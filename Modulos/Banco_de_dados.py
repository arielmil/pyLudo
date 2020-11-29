# coding: utf-8

import mysql.connector as mysql

def Exporta_Conexao(debug = False):
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
        print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        return -2
    return 0

def Deleta_Informacoes(cursor, debug = False):
    '''Para ser chamada ao final de cada partida.'''
    try:
        cursor.execute("TRUNCATE TABLE pyLudo.posicoes")
        
    except mysql.Error as err:
        if (debug):
            print("\n\nErro generico: %s"%err.msg)
        exit(1)
    except AttributeError:
        if (debug):
            print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        exit(2)
    
    return 0


def Salva_Jogador(cursor, jogador, debug = False):
    """Salva na base um jogador, com seus respectivos peões e suas posições iniciais."""
    for i in range(0,4):
        try:
            cursor.execute("INSERT INTO pyLudo.posicoes jogador = %s, cor = %s, peao = %s, posicao = %s"%(jogador[0]["nome"], jogador[1][i]["cor"], 0, jogador[1][i]["pos"]))

        except mysql.Error as err:        
            if (debug):
                print("\n\nErro generico: %s"%err.msg)
            return -1,
                            
        except AttributeError:
            if (debug):
                print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
            return -2
        
    return 0

def Salva_Jogadores(cursor, jogadores, debug = False):
     """Salva na base todos os jogadores com todos os peões."""
     ok = 0
     for i in range(0,size(jogadores)):
         ok = Salva_Jogador(cursor, jogadores[i], debug)
         if (ok == -1):
             exit(1)
         elif (ok == -2):
             exit(2)
     return 0

def Pega_Posicao_Peao_Cor(cursor, cor, peao, debug = False):
    """Retorna a posicao do peao recebido do jogador da cor recebida."""
    try:
        cursor.execute("SELECT posicao FROM pyLudo.posicoes WHERE cor = %s and peao = %s"%(cor, peao))

    except mysql.Error as err:        
        if (debug):
            print("\n\nErro generico ao pegar o peao %s da cor %s: %s"%(peao, cor, err.msg))
        exit(1)
        
    except AttributeError:
        if (debug):
            print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
        exit(2)
        
    pos = cursor.fetchall()
    
    return pos[0]

def Salva_Posicao_Peao_Cor(cursor, cor, peao, posicao, debug = False):
    """Salva no banco de dados a posicao do peao recebido do jogador da cor recebida."""
    try:
        cursor.execute("INSERT INTO pyLudo.posicoes posicao = %s WHERE cor = %s and peao = %s"%(posicao,cor, peao))
        
    except mysql.Error as err:
        if (debug):
            print("\n\nErro generico ao salvar o peao %s da cor %s: %s"%(peao, cor, err.msg))
        exit(1)
        
    except AttributeError:
            if (debug):
                print("\n\nErro: Cursor inválido. Por favor, tente novamente.")
            exit(2)
        
    return 0
