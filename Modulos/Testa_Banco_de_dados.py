# coding: utf-8

from Banco_de_dados import *
import unittest
import random
import importlib

class Testa_Partida(unittest.TestCase):
    def test_01_Conecta_SGBD_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 01 - SGBD conectado com sucesso.")
        
        db = type(Conecta_SGBD("localhost", "ariel", "123456789",False))
        retorno_esperado = mysql.connection_cext.CMySQLConnection
        self.assertEqual(retorno_esperado, db)
        
    def test_02_Conecta_SGBD_debug_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 02 - SGBD nao conectado por erro no nome do host, e printando informacoes de debug.")
        
        db = Conecta_SGBD("localghost", "ariel", "123456789", True)
        retorno_esperado = -1

        self.assertEqual(retorno_esperado, db)

    def test_03_Conecta_SGBD_debug_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 03 - SGBD nao conectado por erro no nome de usuario, e printando informacoes de debug.")
        
        db = Conecta_SGBD("localhost", "aiel", "123456789", True)
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_04_Conecta_SGBD_debug_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 04 - SGBD nao conectado por senha invalida, e printando informacoes de debug.")
        
        db = Conecta_SGBD("localhost", "ariel", "12345678910", True)
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_05_Cria_Cursor_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 05 - Criacao de cursor bem sucedida.")

        db = Conecta_SGBD("localhost", "ariel", "123456789", False)
        cursor = type(Cria_Cursor(db))
        retorno_esperado = mysql.cursor_cext.CMySQLCursorPrepared
        
        self.assertEqual(retorno_esperado, cursor)

    def test_06_Cria_Cursor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 06 - Criacao de cursor mal sucedida por SGBD nao conectado por erro no nome do host, e printando informacoes de debug.")

        db = Conecta_SGBD("localghost", "ariel", "123456789", True)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_07_Cria_Cursor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 07 - Criacao de cursor mal sucedida por SGBD nao conectado por erro no nome de usuario, e printando informacoes de debug.")

        db = Conecta_SGBD("localhost", "aiel", "123456789", True)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_08_Cria_Cursor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 08 - Criacao de cursor mal sucedida por SGBD nao conectado por senha invalida, e printando informacoes de debug.")

        db = Conecta_SGBD("localhost", "ariel", "12345678910", True)
        cursor = Cria_Cursor(db)
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, cursor)

    def test_09_Cria_Tabela_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 09 - Criacao de tabela bem sucedida")

        db = Conecta_SGBD("localhost", "ariel", "123456789", False)
        db.database = "pyLudo"
        cursor = Cria_Cursor(db)
        checagem = Cria_Tabela(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_10_Cria_Tabela_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 10 - Tabela ja existe, e printando informacoes de debug.")

        db = Conecta_SGBD("localhost", "ariel", "123456789", True)
        db.database = "pyLudo"
        cursor = Cria_Cursor(db)
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)
      
    def test_11_Cria_Tabela_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 11 - Tabela nao criada por cursor invalido, e printando informacoes de debug.")

        db = Conecta_SGBD("localhost", "ariel", "123456789", True)
        db.database = "pyLudo"
        cursor = -1
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = -2
        
        self.assertEqual(retorno_esperado, checagem)

    def test_12_Cria_Banco_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 12 - Criacao de Banco de dados bem sucedida.")

        db = Conecta_SGBD("localhost", "ariel", "123456789", False)
        cursor = Cria_Cursor(db)
        checagem = Cria_Banco(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_13_Cria_Banco_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 13 - Banco de dados ja existe, e printando informacoes de debug.")

        db = Conecta_SGBD("localhost", "ariel", "123456789", True)
        cursor = Cria_Cursor(db)
        checagem = Cria_Banco(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_14_Cria_Banco_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 14 - Banco de dados nao criado por cursor invalido, e printando informacoes de debug.")

        db = Conecta_SGBD("localghost", "ariel", "123456789", True)
        cursor = Cria_Cursor(db)
        checagem = Cria_Banco(cursor, True)
        
        retorno_esperado = -2
        
        self.assertEqual(retorno_esperado, checagem)

    def test_15_Exporta_conexao_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 15 - Todas as funcoes anteriores testadas com sucesso, e Exporta_conexao testada com sucesso.")

        conexao = Exporta_Conexao()
        retorno_esperado = dict

        self.assertEqual(retorno_esperado, type(conexao))
        
if __name__ == '__main__':
    unittest.main()
