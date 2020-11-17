from Banco_de_dados import *
import unittest
import random
import importlib

class Testa_Partida(unittest.TestCase):
    def test_01_Conecta_Banco_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 01 - Banco conectado com sucesso.")
        
        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        retorno_esperado = mysql.connection_cext.CMySQLConnection
        
        self.assertIsInstance(retorno_esperado, db)
        
    def test_02_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 02 - Banco nao conectado por erro no nome do host, e printando opcoes de debug.")
        
        db = Conecta_Banco(True, "localghost", "ariel", "123456789")
        retorno_esperado = -1

        self.assertEqual(retorno_esperado, db)

    def test_03_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 03 - Banco nao conectado por erro no nome de usuario, e printando opcoes de debug.")
        
        db = Conecta_Banco(True, "localhost", "aiel", "123456789")
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_04_Conecta_Banco_debug_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 04 - Banco nao conectado por senha invalida, e printando opcoes de debug.")
        
        db = Conecta_Banco(True, "localhost", "ariel", "12345678910")
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, db)

    def test_05_Cria_Cursor_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 05 - Criacao de cursor bem sucedida.")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        cursor = Cria_cursor(db)
        retorno_esperado = mysql.cursor_cext.CMySQLCursor
        
        self.assertIsInstance(retorno_esperado, cursor)

    def test_06_Cria_Tabela_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 06 - Criacao de tabela bem sucedida")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        db.database = "pyLudo"
        cursor = Cria_cursor(db)
        checagem = Cria_Tabela(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_07_Cria_Tabela_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 07 - Tabela ja existe")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        db.database = "pyLudo"
        cursor = Cria_cursor(db)
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)
      
    def test_08_Cria_Tabela_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 08 - Tabela nao criada por cursor invalido.")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        db.database = "pyLudo"
        cursor = 1
        checagem = Cria_Tabela(cursor, True)
        
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, checagem)

    def test_09_Cria_Database_NO(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 09 - Criacao de Database bem sucedida.")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        cursor = Cria_cursor(db)
        checagem = Cria_Database(cursor)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_10_Cria_Database_NO(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 10 - Database ja existe.")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        cursor = Cria_cursor(db)
        checagem = Cria_Database(cursor, True)
        
        retorno_esperado = 0
        
        self.assertEqual(retorno_esperado, checagem)

    def test_11_Cria_Database_NOK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 11 - Database nao criada por cursor invalido.")

        db = Conecta_Banco(False, "localhost", "ariel", "123456789")
        cursor = -1
        checagem = Cria_Database(cursor, True)
        
        retorno_esperado = -1
        
        self.assertEqual(retorno_esperado, checagem)

    def test_12_Exporta_conexao_OK(self):
        print("Teste Modulo Banco de Dados - Caso de Teste 12 - Todas as funcoes anteriores testadas com sucesso, e Exporta_conexao testada com sucesso.")

        conexao = Exporta_conexao()        
        retorno_esperado = "dict"

        self.assertIsInstance(retorno_esperado, conexao)
        
if __name__ == '__main__':
    unittest.main()
