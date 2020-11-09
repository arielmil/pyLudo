from Partida import *
import unittest
import random
import importlib

'''Arquivo de testes do módulo Partida'''

class Testa_Dado(unittest.TestCase):
    
    def test_01_Manda_para_casa_OK(self):
        peao = {"cor":"branco", "act_pos":2, "fin_pos": 5, "sprite": '../../Assets/peão'+'_' + "branco" +'.png'}
        teste =  Manda_para_casa(peao)

        print("Caso de Teste 01 - O peão retorna para a posição 0")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_02_Manda_para_casa_NOK(self):
        peao = ["branco",5]
        teste = Manda_para_casa(peao)

        print("Caso de Teste 02 - O peão nao é um dicionário e por isso não volta para posição inicial")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    '''def test_03_Captura_Peao_OK(self):
        peao = {"cor":"branco", "act_pos":2, "fin_pos": 5, "sprite": '../../Assets/peão'+'_' + "branco" +'.png'}
        teste = Captura_peao(peao)

        print("Caso de Teste 03 - Captura peão corretamente")
        resultado_esperado = 0
        self.assertEqual(retorno_esperado, teste)'''


        
if __name__ == '__main__':
    unittest.main()

