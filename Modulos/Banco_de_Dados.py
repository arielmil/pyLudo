import mysql.connector as mysql

def Conecta_Banco()
    db = mysql.connect(host = "localhost", user = "ariel", passwd = "123456789")
    return db

def Salva_jogador():
    """Salva o nome do usuário que foi cadastrado"""
    return 0
    
def Salva_partida():
    """Salva o histórico de partidas"""
    return 0
