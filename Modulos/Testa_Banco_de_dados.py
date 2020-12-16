# coding: utf-8

from Banco_de_dados import *
from Peao import Cria_peoes
import unittest

class Testa_Partida(unittest.TestCase):
    def test_01_Conecta_SGBD_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 01 - SGBD conectado com sucesso.")
        
        db = type(Conecta_SGBD("localhost", "ariel", "123456789"))
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

        db = Conecta_SGBD("localhost", "ariel", "123456789")
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

        db = Conecta_SGBD("localhost", "ariel", "123456789")
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

        db = Conecta_SGBD("localhost", "ariel", "123456789")
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

    def test_16_Deleta_Informacoes_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 16 - Deleta_Informacoes funcionando com sucesso.")

        db = Exporta_Conexao()
        retorno_esperado = 0
        checa = Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, checa)

    def test_17_Deleta_Informacoes_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 17 - Deleta_Informacoes falhando por cursor invalido, e printando informacoes de debug.")

        db = {"cursor": -1}
        retorno_esperado = -2
        checa = Deleta_Informacoes(db, True)

        self.assertEqual(retorno_esperado, checa)
        
    def test_18_Salva_Jogador_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 18 - Salva_Jogador funcionando com sucesso.")

        db = Exporta_Conexao()
        player = {"nome": "Jogador 1"}
        peoes = Cria_peoes("vermelho")
        jogador = [player,peoes]

        checa = Salva_Jogador(db, jogador)
        resultado_consulta_teorica = [("Jogador 1", "vermelho", 0, 0), ("Jogador 1", "vermelho", 1, 0), ("Jogador 1", "vermelho", 2, 0), ("Jogador 1", "vermelho", 3, 0)]
        
        db["cursor"].execute("SELECT * from pyLudo.posicoes")
        resultado_real = db["cursor"].fetchall()
        
        Deleta_Informacoes(db)
        
        if (checa == 0):
            self.assertEqual(resultado_consulta_teorica, resultado_real)
        else:
            self.assertEqual(1,0)

    def test_19_Salva_Jogador_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 19 - Salva_Jogador falhando por cursor invalido, e printando informacoes de debug.")

        db = {"cursor": -1}
        player = {"nome": "Jogador 1"}
        peoes = Cria_peoes("vermelho")
        jogador = [player,peoes]

        checa = Salva_Jogador(db, jogador, True)
        retorno_esperado = -2

        self.assertEqual(retorno_esperado, checa)

    def test_20_Salva_Jogadores_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 20 - Salva_Jogadores funcionando com sucesso.")

        db = Exporta_Conexao()
        
        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        checa = Salva_Jogadores(db, jogadores)
        retorno_esperado = 0
        
        Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, checa)

    def test_21_Salva_Jogadores_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 21 - Salva_Jogadores falhando por cursor invalido, e printando informacoes de debug.")

        db = {"cursor": -1}
        
        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        checa = Salva_Jogadores(db, jogadores, True)
        retorno_esperado = -2
        
        Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, checa)

    def test_22_Salva_Posicao_Peao_Cor_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 22 - Salva_Posicao_Peao_Cor funcionando com sucesso.")

        db = Exporta_Conexao()

        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        Salva_Jogadores(db, jogadores)
        db["cursor"].execute("SELECT * FROM pyLudo.posicoes")
        antes = db["cursor"].fetchall()
        
        cor = peoes1[0]["cor"]
        checagem = Salva_Posicao_Peao_Cor(db, cor, 0, 1)
        
        db["cursor"].execute("SELECT * FROM pyLudo.posicoes")
        depois = db["cursor"].fetchall()

        Deleta_Informacoes(db)
        
        if (checagem == 0):
            self.assertNotEqual(antes, depois)
        else:
            self.assertEqual(1, -1)

    def test_23_Salva_Posicao_Peao_Cor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 23 - Salva_Posicao_Peao_Cor falhando por cursor invalido, e printando informacoes de debug.")
        db = {"cursor": -1}

        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}

        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        cor = peoes1[0]["cor"]
        checagem = Salva_Posicao_Peao_Cor(db, cor, 0, 9, True)
        retorno_esperado = -2

        Deleta_Informacoes(db)

        self.assertEqual(checagem, retorno_esperado)
        
    def test_24_Pega_Posicao_Peao_Cor_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 24 - Pega_Posicao_Peao_Cor funcionando com sucesso.")

        db = Exporta_Conexao()
        cursor = db["cursor"]

        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        Salva_Jogadores(db, jogadores)
        
        cor = peoes1[0]["cor"]
        Salva_Posicao_Peao_Cor(db, cor, 0, 9)

        retorno_esperado = 9
        pos = Pega_Posicao_Peao_Cor(cursor, cor, 0)

        Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, pos)
        
    def test_25_Pega_Posicao_Peao_Cor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 25 - Pega_Posicao_Peao_Cor falhando por cursor invalido, e printando informacoes de debug.")

        db = Exporta_Conexao()
        cursor = db["cursor"]

        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        Salva_Jogadores(db, jogadores)
        
        cor = peoes1[0]["cor"]
        Salva_Posicao_Peao_Cor(db, cor, 0, 9)
     
        cursor = -1
        retorno_esperado = -2
        pos = Pega_Posicao_Peao_Cor(cursor, cor, 0, True)

        Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, pos)
        
    def test_26_Pega_Posicoes_Peoes_Cor_OK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 26 - Pega_Posicoes_Peao_Cor funcionando com sucesso.")
        
        db = Exporta_Conexao()
        cursor = db["cursor"]
        
        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        Salva_Jogadores(db, jogadores)
        
        cor = peoes1[0]["cor"]
        Salva_Posicao_Peao_Cor(db, cor, 0, 9)
        Salva_Posicao_Peao_Cor(db, cor, 1, 10)
        Salva_Posicao_Peao_Cor(db, cor, 2, 11)
        Salva_Posicao_Peao_Cor(db, cor, 3, 12)
        
        retorno_esperado = [9,10,11,12]
        posicoes = Pega_Posicoes_Peoes_Cor(cursor, cor)

        Deleta_Informacoes(db)

        self.assertEqual(retorno_esperado, posicoes)

    def test_27_Pega_Posicoes_Peao_Cor_NOK(self):
        print("\nTeste Modulo Banco de Dados - Caso de Teste 27 - Pega_Posicoes_Peao_Cor falhando por cursor invalido, e printando informacoes de debug.")

        db = Exporta_Conexao()
        cursor = db["cursor"]
        
        player1 = {"nome": "Jogador 1"}
        player2 = {"nome": "Jogador 2"}
        player3 = {"nome": "Jogador 3"}
        player4 = {"nome": "Jogador 4"}
        
        peoes1 = Cria_peoes("vermelho")
        peoes2 = Cria_peoes("amarelo")
        peoes3 = Cria_peoes("azul")
        peoes4 = Cria_peoes("verde")

        jogadores = [[player1, peoes1],[player2, peoes2],[player3, peoes3],[player4, peoes4]]

        Salva_Jogadores(db, jogadores)
        
        cor = peoes1[0]["cor"]
        Salva_Posicao_Peao_Cor(db, cor, 0, 9)
        Salva_Posicao_Peao_Cor(db, cor, 1, 10)
        Salva_Posicao_Peao_Cor(db, cor, 2, 11)
        Salva_Posicao_Peao_Cor(db, cor, 3, 12)

        cursor = -1
        retorno_esperado = -2
        posicoes = Pega_Posicoes_Peoes_Cor(cursor, cor, True)

        self.assertEqual(retorno_esperado, posicoes)
        
if __name__ == '__main__':
    unittest.main()
