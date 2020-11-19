# coding: utf-8

import mysql.connector as mysql

def Exporta_Conexao(debug1 = False, debug2 = False, debug3 = False):
    db = Conecta_Banco("localhost","ariel","123456789",debug1)
    cursor = 0
    checagem = 0
    
    if (db == -1):
        input("\n(Pressione enter para fechar o programa)")
        exit(1)
    elif (db == -2):
        input("\n(Pressione enter para fechar o programa)")
        exit(2)

    cursor = Cria_Cursor(db)
    if (cursor == -1):
        input("\n(Pressione enter para fechar o programa)")
        exit(1)
    
    checagem = Cria_Database(cursor,debug2)
    if (checagem == -1):
        print("oi")
        input("\nPressione enter para fechar o programa)")
        exit(1)

    db.database = "pyLudo"
    checagem = Cria_Tabela(cursor,debug3)

    if (checagem == -1):
        input("\nPressione enter para fechar o programa)")
        
    return {"db":db, "cursor":cursor}

def Conecta_Banco(h, u, p, debug = False):
    try:
        db = mysql.connect(host = h, user = u, passwd = p)
    except mysql.Error as err:
        if (debug):
            print(vars(err))
        if err.errno == 2005 and err.sqlstate == "HY000":
            print("\nErro: host com nome desconhecido. Tente novamente mais tarde.")
            return -1
        elif err.errno == 1045 and err.sqlstate == "28000":
            print("\nErro: acesso negado para este user. Tente novamente mais tarde.")
            return -2
    else:
        return db

def Cria_Cursor(db):
    if (type(db) != mysql.connection_cext.CMySQLConnection):
        print("Erro: Banco de dados invalido. Por favor, tente novamente.")
        return -1
    cursor = db.cursor(prepared=True)
    return cursor

def Cria_Database(cursor, debug = False):
    try:
        cursor.execute("CREATE DATABASE pyLudo")
    except mysql.Error as err:
        if (debug):
            print(vars(err))
        if (err.errno != 1007 and err.sqlstate != "HY000") and (err.errno != -1 and err.sqlstate != None):
            print("Erro: ",err.msg)
            return -1
    except AttributeError:
        print("Erro: cursor inválido. Por favor, tente novamente.")
        return -1
    return 0

def Cria_Tabela(cursor, debug = False):
    try:
        cursor.execute("CREATE TABLE pyLudo.posicoes (jogador VARCHAR(31), cor VARCHAR(20), peao SMALLINT, posicao SMALLINT, PRIMARY KEY (jogador, cor, peao, posicao))")
    except mysql.Error as err:
        if(debug):
            print(vars(err))
        if (err.errno != 1050 and err.sqlstate != "42S01") and (err.errno != -1 and err.sqlstate != None):
                print(vars(err))
                return -1
    except AttributeError:
        print("Erro: Cursor inválido. Por favor, tente novamente.")
        return -1
    return 0

def Deleta_Informacoes(cursor, debug = False):
    '''Para ser chamada ao final de cada partida.'''
    try:
        cursor.execute("TRUNCATE TABLE pyLudo.posicoes")
        
    except mysql.Error as err:
        print("Erro inesperado. Por favor, tente novamente mais tarde.")
        if (debug):
            print(vars(err)+"\n\n"+err.msg)
            return -1
        
    except AttributeError:
        print(cursor)
        print("Erro: Cursor inválido. Por favor, tente novamente.")
        return -2
    
    return 0


def Salva_Jogador(cursor, jogador, debug = False):
    """Salva na base um jogador, com seus respectivos peões e suas posições iniciais."""
    for i in range(0,4):
        try:
            cursor.execute("INSERT INTO posicoes jogador = %s, cor = %s, peao = %s, posicao = %s"%(jogador[0]["nome"], jogador[1][i]["cor"], 0, jogador[1][i]["pos"]))

        except mysql.Error as err:
            print("Erro inesperado inserindo o peão %d. Por favor, tente novamente mais tarde."%i)
        
            if (debug):
                print(vars(err)+"\n\n"+err.msg)
                return -1
        
        except AttributeError:
            print("Erro: Cursor inválido. Por favor, tente novamente.")
            return -2
        
    return 0

def Salva_Jogadores(cursor, jogadores, debug = False):
     """Salva na base todos os jogadores com todos os peões."""
     ok = 0
     for i in range(0,size(jogadores)):
         if (ok == 0):
             ok = Salva_Jogador(cursor, jogadores[i], debug)
         else:
             return -1
     return 0

def Salva_partida():
    """Salva o histórico de partidas."""
    return 0

a = Exporta_Conexao()
Deleta_Informacoes(a["db"],True)
