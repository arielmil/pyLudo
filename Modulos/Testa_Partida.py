from Partida import *
from Peao import *
import unittest
import random
import importlib

'''Arquivo de testes do módulo Partida'''

class Testa_Partida(unittest.TestCase):
    
    def test_01_Manda_para_casa_OK(self):
        peao = Cria_peao("branco",5)
        teste =  Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 01 - O peão retorna para a posição 0")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_02_Manda_para_casa_NOK(self):
        peao = ["branco",5]
        teste = Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 02 - O peão não é um dicionário e por isso não volta para posição inicial")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_03_Nao_Captura_Peao_OK(self):
        peao_1 = Cria_peao("branco",5)
        peao_2 = Cria_peao("vermelho",2)
        tabuleiro[5]["peoes"] = [peao_1]
        teste = Captura_peao(peao_1)

        print("Teste Módulo Partida - Caso de Teste 03 - Não há peões para serem capturados nessa casa")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)
        
    def test_04_Captura_Peao_OK(self):
        peao_1 = Cria_peao("branco",1)
        peao_2 = Cria_peao("vermelho",1)
        tabuleiro[1]["peoes"] = [peao_1,peao_2]
        teste = Captura_peao(peao_1)
       
        print("Teste Módulo Partida - Caso de Teste 04 - Peão é capturado com sucesso")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_05_Captura_Peao_NOK(self):
        peao = Cria_peao("branco",59)
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 05 - fin_pos não e um valor válido - MAIOR QUE 57")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_06_Captura_Peao_NOK(self):
        peao = Cria_peao("branco",-1)
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 06 - fin_pos não e um valor válido - MENOR QUE 0")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_07_Captura_Peao_NOK(self):
        peao = {"teste": 2, "modular": 5}
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 07 - fin_pos não existe")
        retorno_esperado = -4
        self.assertEqual(retorno_esperado, teste)

    def test_08_Captura_Peao_NOK(self):
        peao = 1
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 08 - Peão não e um dicionário")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_09_Roda_tabuleiro_NOK(self):
        tabuleiro = []
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 09 - Tabuleiro é uma lista vazia")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_10_Roda_tabuleiro_NOK(self):
        casa = {"x": -2, "y": 0, "peoes": [], "semi_torres": [], "torres": []}
        tabuleiro = Cria_tabuleiro(casa,2)
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 10 - Posição da casa em que se encontra é negativa em x")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

    def test_11_Roda_tabuleiro_NOK(self):
        casa = {"x": 0, "y": -5, "peoes": [], "semi_torres": [], "torres": []}
        tabuleiro = Cria_tabuleiro(casa,2)
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 11 - Posição da casa em que se encontra é negativa em y")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)
        
if __name__ == '__main__':
    unittest.main()

