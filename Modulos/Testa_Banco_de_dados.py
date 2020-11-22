# coding: utf-8

from Banco_de_dados import *
import unittest
import random
import importlib

class Testa_Partida(unittest.TestCase):
    def test_01_Conecta_Banco_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 01 - Banco conectado com sucesso.")
        
        db = type(Conecta_Banco("localhost", "ariel", "123456789",False))
        retorno_esperado = mysql.connection_cext.CMySQLConnection
        self.assertEqual(retorno_esperado, db)
        
    def test_02_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 02 - Banco nao conectado por erro no nome do host, e printando opcoes de debug.")
        
        db = Conecta_Banco("localghost", "ariel", "123456789", True)
        retorno_esperado = -1

        self.assertEqual(retorno_esperado, db)

    def test_03_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 03 - Banco nao conectado por erro no nome de usuario, e printando opcoes de debug.")
        
        db = Conecta_Banco("localhost", "aiel", "123456789", True)
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_04_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 04 - Banco nao conectado por senha invalida, e printando opcoes de debug.")
        
        db = Conecta_Banco("localhost", "ariel", "12345678910", True)
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_05_Cria_Cursor_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 05 - Criacao de cursor bem sucedida.")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        cursor = type(Cria_Cursor(db))
        retorno_esperado = mysql.cursor_cext.CMySQLCursorPrepared
        
        self.assertEqual(retorno_esperado, cursor)

    def test_06_Cria_Cursor_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 06 - Criacao de cursor mal sucedida por banco nao conectado por erro no nome do host.")

        db = Conecta_Banco("localghost", "ariel", "123456789", False)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_07_Cria_Cursor_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 07 - Criacao de cursor mal sucedida por banco nao conectado por erro no nome de usuario.")

        db = Conecta_Banco("localhost", "aiel", "123456789", False)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_08_Cria_Cursor_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 08 - Criacao de cursor mal sucedida por banco nao conectado por senha invalida.")

        db = Conecta_Banco("localhost", "ariel", "12345678910", False)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_09_Cria_Tabela_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 09 - Criacao de tabela bem sucedida")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        db.database = "pyLudo"
        cursor = Cria_Cursor(db)
        checagem = Cria_Tabela(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_10_Cria_Tabela_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 10 - Tabela ja existe")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        db.database = "pyLudo"
        cursor = Cria_Cursor(db)
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)
      
    def test_11_Cria_Tabela_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 11 - Tabela nao criada por cursor invalido.")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        db.database = "pyLudo"
        cursor = -1
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, checagem)

    def test_12_Cria_Database_NO(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 12 - Criacao de Database bem sucedida.")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        cursor = Cria_Cursor(db)
        checagem = Cria_Database(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_13_Cria_Database_NO(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 13 - Database ja existe.")

        db = Conecta_Banco("localhost", "ariel", "123456789", False)
        cursor = Cria_Cursor(db)
        checagem = Cria_Database(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_14_Cria_Database_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 14 - Database nao criada por cursor invalido.")

        db = Conecta_Banco("localghost", "ariel", "123456789", False)
        cursor = Cria_Cursor(db)
        checagem = Cria_Database(cursor, True)
        
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, checagem)

    def test_15_Exporta_conexao_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 15 - Todas as funcoes anteriores testadas com sucesso, e Exporta_conexao testada com sucesso.")

        conexao = Exporta_Conexao()
        retorno_esperado = dict

        self.assertEqual(retorno_esperado, type(conexao))
        
if __name__ == '__main__':
    unittest.main()
