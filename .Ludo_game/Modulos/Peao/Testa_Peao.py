from Peao import *
import unittest

'''Arquivo de testes do módulo Peao'''

class Testa_Peao(unittest.TestCase):

    def test_01_inicializa_peao_OK(self):
        
        teste = Inicializa_peao("branco", 5)

        print("Caso de Teste 01 - Criar um peão com sucesso")
        retorno_esperado = {"cor":"branco", "act_pos":5, "fin_pos": 5, "sprite": '../../Assets/peão_branco.png'}
        self.assertEqual(retorno_esperado, teste)
    
    def test_02_mover_peao_OK(self):
        
        teste = Inicializa_peao("branco", 0)
        
        print("Caso de Teste 02 - Mover Peão com sucesso")
        retorno_esperado = Move_peao(teste, 5)
        self.assertEqual(retorno_esperado, 0)
        
    def test_03_mover_peao_casa_57(self):
        
        teste = Inicializa_peao("branco", 55)
        
        print("Caso de Teste 03 - Peão não ultrapassa última casa")
        retorno_esperado = Move_peao(teste, 2)
        self.assertEqual(retorno_esperado, 0)

    def test_04_mover_peao_casa_acima_de_57(self):
        
        teste = Inicializa_peao("branco", 55)
        
        print("Caso de Teste 04 - Peão ultrapassa última casa")
        retorno_esperado = Move_peao(teste, 5)
        self.assertEqual(retorno_esperado, -2)

    def test_05_mover_peao_zero_casas(self):
        
        teste = Inicializa_peao("branco", 0)
        
        print("Caso de Teste 05 - Dado com número 0")
        retorno_esperado = Move_peao(teste, 0)
        self.assertEqual(retorno_esperado, -1)
        
    def test_06_mover_peao_casa_negativa(self):
        
        teste = Inicializa_peao("branco", 0)
        
        print("Caso de Teste 06 - Dado com número negativo")
        retorno_esperado = Move_peao(teste, -2)
        self.assertEqual(retorno_esperado, -1)

    def test_07_mover_peao_casa_acima_6(self):
        
        teste = Inicializa_peao("branco", 0)
        
        print("Caso de Teste 07 - Dado com número acima de 6")
        retorno_esperado = Move_peao(teste, 8)
        self.assertEqual(retorno_esperado, -1)
        

if __name__ == '__main__':
    unittest.main()

