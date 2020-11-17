import mysql.connector as mysql

def Exporta_conexao():
    db = Conecta_Banco(True)
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
    
    checagem = Cria_Database(cursor)
    if (checagem == -1):
        input("\nPressione enter para fechar o programa)")
        exit(1)

    db.database = "pyLudo"
    checagem = Cria_Tabela(cursor)

    if (checagem == -1):
        input("\nPressione enter para fechar o programa)")
        
    return {"db":db, "cursor":cursor}

def Conecta_Banco(debug=False):
    try:
        db = mysql.connect(host = "localhost", user = "ariel", passwd = "123456789")
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
    if (db != -1 and db != -2):
        cursor = db.cursor()
        return cursor
    else:
        return -1

def Cria_Database(cursor, debug=False):
    try:
        cursor.execute("CREATE DATABASE pyLudo")
    except mysql.Error as err:
        if (debug):
            print(vars(err))
        if err.errno != 1007 and err.sqlstate != "HY000":
            print("Erro: ",err.msg)
            return -1
    return 0

def Cria_Tabela(cursor, debug=False):
    try:
        cursor.execute("CREATE TABLE posicoes (jogador VARCHAR(31), cor VARCHAR(20), peao SMALLINT, PRIMARY KEY (jogador, cor, peao))")
    except mysql.Error as err:
        if(debug):
            print(vars(err))
        if err.errno != 1050 and err.sqlstate != "42S01":
                print(vars(err))
                return -1
    return 0

def Salva_jogador():
    """Salva o nome do usuário que foi cadastrado"""
    return 0
    
def Salva_partida():
    """Salva o histórico de partidas"""
    return 0
