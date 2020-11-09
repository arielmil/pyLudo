from Dados import *
import unittest
import random


'''Arquivo de testes do módulo Dado'''

class Testa_Dado(unittest.TestCase):
    
    def test_01_Cria_dado_vermelho_OK(self):
        teste = Cria_dado("vermelho")

        print("Caso de Teste 01 - Criar um elemento dado vermelho")
        retorno_esperado = {"num": None, "sprites": ['../../Assets/Dado_vermelho/dice_1.png',
                    '../../Assets/Dado_vermelho/dice_2.png',
                    '../../Assets/Dado_vermelho/dice_3.png',
                    '../../Assets/Dado_vermelho/dice_4.png',
                    '../../Assets/Dado_vermelho/dice_5.png',
                    '../../Assets/Dado_vermelho/dice_6.png']}
        self.assertEqual(retorno_esperado, teste)

    def test_02_Cria_dado_branco_OK(self):
        teste = Cria_dado("branco")

        print("Caso de Teste 02 - Criar um elemento dado branco")
        retorno_esperado = {"num": None, "sprites": ['../../Assets/Dado_branco/dice_1.png',
                    '../../Assets/Dado_branco/dice_2.png',
                    '../../Assets/Dado_branco/dice_3.png',
                    '../../Assets/Dado_branco/dice_4.png',
                    '../../Assets/Dado_branco/dice_5.png',
                    '../../Assets/Dado_branco/dice_6.png']}
        self.assertEqual(retorno_esperado, teste)
        
    def test_03_num_dado_OK(self):
        teste = Cria_dado("vermelho")

        print("Caso de Teste 03 - Número do dado está no entre [1,6]")
        retorno_esperado = Clica_dado(teste)
        self.assertEqual(retorno_esperado, 0)
        


if __name__ == '__main__':
    unittest.main()

