# coding: utf-8

import mysql.connector as mysql

def Exporta_Conexao(debug = False):
    """Recebe um booleno chamado debug (False por padrão). Cria, ou retorna todos os dados necessários para o uso do banco de dados em um dicionário contendo dois campos: db que armazena um ponteiro para o SGBD configurado para o banco de dados pyLudo, e cursor que armazena um cursor para este SGBD, ou sai do jogo com um código de erro caso o contrário (código de erro 1 para: Erro no nome do host para conexão com o SGBD, criação do cursor, criação do Banco de dados, ou criação da tabela. Ou código de erro 2 para: Erros no nome de usuário ou senha ou algum erro genérico para conexão com o SGBD, ou de cursor inválido). Printa informações de erro caso debug seja True."""
    
    db = Conecta_SGBD("localhost","ariel","123456789",debug)
    cursor = 0
    checagem = 0
    
    if (db == -1):
        input("\n(Pressione enter para fechar o programa)")
        exit(1)
    elif (db == -2 or db == -3):
        input("\n(Pressione enter para fechar o programa)")
        exit(2)

    cursor = Cria_Cursor(db, debug)
    if (cursor == -1 or cursor == -2):
        input("\n(Pressione enter para fechar o programa)")
        exit(1)
    
    checagem = Cria_Banco(cursor,debug)
    if (checagem == -1):
        input("\nPressione enter para fechar o programa)")
        exit(1)
    elif (checagem == -2):
        input("\nPressione enter para fechar o programa)")
        exit(2)

    db.database = "pyLudo"
    checagem = Cria_Tabela(cursor,debug)

    if (checagem == -1):
        input("\nPressione enter para fechar o programa)")
        exit(1)
    elif (checagem == -2):
        input("\n\nPressione enter para fechar o programa)")
        exit(2)
        
    return {"db":db, "cursor":cursor}

def Conecta_SGBD(h, u, p, debug = False):
    """Recebe quatro strings: h (host), u (usuário), p (senha), e um booleno chamado debug (False por padrão). Conecta com o SBGD. Retorna um ponteiro para ele em caso de sucesso, -1 em caso de erro por host inválido, -2 em caso de erro nos campos user ou senha, ou -3 em caso de erros genéricos. Printa informações de erro caso debug seja True."""
    
    try:
        db = mysql.connect(host = h, user = u, passwd = p)
    except mysql.Error as err:
        if err.errno == 2005 and err.sqlstate == "HY000":
            if (debug):
                print("\n\nErro: host com nome desconhecido. Tente novamente.")
            return -1
        elif err.errno == 1045 and err.sqlstate == "28000":
            if (debug):
                print("\n\nErro: acesso negado para este user. Tente novamente.")
            return -2
        else:
            if (debug):
                 print("\n\nErro generico: %s"%err.msg)
            return -3
    else:
        return db

def Cria_Cursor(db, debug = False):
    """Recebe um ponteiro para o SGBD, e um booleano chamado debug (False por padão). Cria um cursor (objeto de Banco de Dados). Retorna o cursor em caso de sucesso, -1 em caso de erro por conexão ao SGBD, ou -2 em caso de erros genéricos."""
    
    if (type(db) != mysql.connection_cext.CMySQLConnection):
        if (debug):
            print("Erro: Problemas na conexao com o SGBD. Por favor, tente novamente.")
        return -1
    try:
        cursor = db.cursor(prepared=True)
    except mysql.Error as err:
        if (debug):
            print("\n\nErro generico: %s"%err.msg)
        return -2
    
    return cursor

def Cria_Banco(cursor, debug = False):
    """Recebe um cursor, e um booleno chamado debug (False por padrão). Cria um banco de dados chamado pyGames (ou não faz nada caso esse banco já exista). Retorna 0 em caso de sucesso, -1 em caso de erros genéricos, ou -2 em caso de erro por cursor inválido."""
    
    try:
        cursor.execute("CREATE DATABASE pyLudo")
    except mysql.Error as err:
        if (err.errno != 1007 and err.sqlstate != "HY000") and (err.errno != -1 and err.sqlstate != None):
            if (debug):
                print("\n\nErro generico: %s"%err.msg)
            return -1
        else:
            if (debug):
                print("\n\nBanco ja existe.")
    except AttributeError:
        if (debug):
            print("\n\nErro: cursor inválido. Por favor, tente novamente.")
        return -2
    return 0

def Cria_Tabela(cursor, debug = False):
    """Recebe um cursor, e um booleno chamado debug (False por padrão). Cria uma tabela para guardar dados de jogador dentro do banco de dados (ou não faz nada caso essa tabela já exista). Retorna 0 em caso de sucesso, -1 em caso de erros genericos, ou -2 em caso de erro por cursor inválido. Printa informações de erros caso debug seja True."""
    
    try:
        cursor.execute("CREATE TABLE pyLudo.posicoes (jogador VARCHAR(31), cor VARCHAR(20), peao SMALLINT, posicao SMALLINT, PRIMARY KEY (cor, peao))")
    except mysql.Error as err:
        if (err.errno != 1050 and err.sqlstate != "42S01") and (err.errno != -1 and err.sqlstate != None):
            if (debug):
                 print("\n\nErro generico: %s"%err.msg)
                 return -1
        else:
            if (debug):
                print("\n\nTabela ja existe.")
    except AttributeError:
        if (debug):
            print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        return -2
    return 0

def Deleta_Informacoes(db, debug = False):
    """Deve ser chamada pelo módulo Main ao final de cada partida. Recebe uma variável chamada db (um dicionário conténdo um ponteiro para o banco de dados, e um cursor para o mesmo), e um booleano chamado debug (False por padrão). Deleta todas as informações salvas na tabela Jogadores do Banco, mantendo somente sua estrutura semantica (Primary Keys, Foreign Keys, etc...). Retorna 0 caso seja bem sucedido, -1 para erros genericos, ou -2 em caso de erro por cursor inválido. Printa informações de erro caso debug seja True."""

    try:
        db["cursor"].execute("TRUNCATE TABLE pyLudo.posicoes")
        db["db"].commit()
        db["cursor"].close()
        
    except:
        try:
            db["cursor"].close()
            db["cursor"] = Cria_Cursor(db["db"])
            db["cursor"].execute("TRUNCATE TABLE pyLudo.posicoes")
            db["db"].commit()
            db["cursor"].close()
        except mysql.Error as err:
            if (debug):
                print("\n\nErro generico: %s"%err.msg)
            return -1
        except AttributeError:
            if (debug):
                print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
            return -2
    return 0


def Salva_Jogador(db, jogador, debug = False):
    """Recebe uma variável chamada db (um dicionário conténdo um ponteiro para o banco de dados, e um cursor para o mesmo), um jogador (um array contendo em seu primeiro índice um player (como definido pelo módulo Player), e em seu segundo índice um array contendo seus quatro peões (como definidos pelo módulo Peão) ), e um booleano chamado debug (False por padrão). Salva no Banco este jogador com a sua cor e seus quatro peões em suas posições iniciais. Retorna 0 em caso de sucesso, -1 em caso de erros genericos, ou -2 em caso de erro por cursor inválido. Printa informações de erro caso debug seja True."""

    for i in range(0,4):
        try:
            sql = "INSERT INTO pyLudo.posicoes (jogador, cor, peao, posicao) VALUES (%s, %s, %s, %s)"
            valores = (jogador[0]["nome"], jogador[1][0]["cor"], i, jogador[1][i]["pos"])
            db["cursor"].execute(sql, valores)
            db["db"].commit()
        except mysql.Error as err:        
            if (debug):
                print("\n\nErro generico: %s"%err.msg)
            return -1,
                            
        except AttributeError:
            if (debug):
                print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
            return -2
        
    return 0

def Salva_Jogadores(db, jogadores, debug = False):
    """Recebe uma variável chamada db (um dicionário conténdo um ponteiro para o banco de dados, e um cursor para o mesmo), um array de jogadores provido pela função Quantos_jogam do módulo Main, e um booleano chamado debug (False por padrão). Itera sobre este array chamando a função Salva_Jogador para cada elemento nele afim de salvar todos os jogadores da partida no Banco. Retorna 0 em caso de sucesso para todos os elementos, -1 para erros genericos em algum elemento, ou -2 em caso de erro por cursor inválido. Printa informações de erro caso debug seja True."""
    
     ok = 0
     for i in range(0,len(jogadores)):
         ok = Salva_Jogador(db, jogadores[i], debug)
         if (ok == -1):
             return -1
         elif (ok == -2):
             return -2
     return 0

def Pega_Posicao_Peao_Cor(cursor, cor, peao_num, debug = False):
    """Recebe um cursor, um peão (como definido pelo módulo Peões), um número inteiro de 0 a 4 representando um dos quatro peões de um jogador, e um booleano chamado debug (False por padrão). Pega no Banco de Dados a posição deste peão para este jogador (conhecido pela sua cor contída na variável peão recebida), e retorna a posição recolhida em caso seja de sucesso, -1 para erros genericos, ou -2 em caso de erro por cursor inválido. Printa informações de erro caso debug seja True."""

    try:
        sql = "SELECT posicao FROM pyLudo.posicoes WHERE cor = %s and peao = %s"
        valores = (cor, peao_num)
        cursor.execute(sql, valores)

    except mysql.Error as err:        
        if (debug):
            print("\n\nErro generico ao pegar a posicao peao %s da cor %s: %s"%(peao_num, cor, err.msg))
        return -1
        
    except AttributeError:
        if (debug):
            print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        return -2
        
    pos = cursor.fetchall()    
    return pos[0][0]
    
def Pega_Posicoes_Peoes_Cor(cursor, cor, debug = False):
    """Recebe um cursor, uma cor (string), e um booleano chamado debug (False por padrão). Pega no Banco de dados as posições dos quatro peões do jogador associado a esta cor, e as retorna em um array, em caso de erro: retorna -1 por erros genéricos, ou -2 por erros por cursor inválido. Printa informações de erro cas debug seja True."""
    
    lista_posicoes = []
    try:
        sql = "SELECT posicao FROM pyLudo.posicoes WHERE cor = '%s'"%(cor)
        cursor.execute(sql)
        
    except mysql.Error as err:
        if (debug):
            print("\n\nErro generico ao pegar as posicoes dos peoes da cor %s: %s"%(cor, err.msg))
            return -1

    except AttributeError:
        if (debug):
            print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        return -2
        
    posicoes = cursor.fetchall()
    
    for pos in posicoes:
        lista_posicoes.append(pos[0])
    
    return lista_posicoes

def Salva_Posicao_Peao_Cor(db, cor, peao_num, posicao, debug = False):
    """Recebe uma variável chamada db (um dicionário conténdo um ponteiro para o banco de dados, e um cursor para o mesmo), um peão (como definido pelo módulo Peoes), um número inteiro de 0 a 4 representando um dos quatro peões de um jogador, a sua posição, e um booleano chamado debug (False por padrão). Salva no banco a posição deste peão para o jogador desta cor (conhecido pela sua cor contída na variável peão recebida), e retorna 0 caso seja bem sucedido, -1 para erros genericos, ou -2 em caso de erro por cursor inválido. Printa informações de erro caso debug seja True."""
    
    try:
        sql = "UPDATE pyLudo.posicoes SET posicao = %s WHERE cor = %s and peao = %s"
        valores = (posicao, cor, peao_num)
        db["cursor"].execute(sql, valores)
        db["db"].commit()
        
    except mysql.Error as err:
        if (debug):
            print("\n\nErro generico ao salvar o peao %s da cor %s: %s"%(peao_num, cor, err.msg))
        return -1
        
    except AttributeError:
            if (debug):
                print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
            return -2
        
    return 0
    
__all__ = ['Salva_Posicao_Peao_Cor', 'Pega_Posicoes_Peoes_Cor', 'Pega_Posicao_Peao_Cor', 'Salva_Jogadores', 'Deleta_Informacoes']
