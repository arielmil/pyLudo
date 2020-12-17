import Peao
import unittest

'''Arquivo de testes do módulo Peao'''

class Testa_Peao(unittest.TestCase):

    def test_01_Cria_peao_OK(self):
        
        teste = Peao.Cria_peao("vermelho", 5)

        print("Caso de Teste 01 - Criar um peão com sucesso")
        retorno_esperado = {"cor":"vermelho", "pos": 5, "sprite": '../Assets/peão_vermelho.png'}
        self.assertEqual(retorno_esperado, teste)
    
    def test_02_mover_peao_OK(self):
        
        teste = Peao.Cria_peao("vermeljo", 0)
        
        print("Teste Módulo Peão - Caso de Teste 02 - Mover Peão com sucesso")
        retorno_esperado = Peao.Move(teste, 5)
        self.assertEqual(retorno_esperado, 0)
        
    def test_03_mover_peao_casa_57(self):
        
        teste = Peao.Cria_peao("vermelho", 55)
        
        print("Teste Módulo Peão - Caso de Teste 03 - Peão não ultrapassa última casa")
        retorno_esperado = Peao.Move(teste, 2)
        self.assertEqual(retorno_esperado, 0)

    def test_04_mover_peao_casa_acima_de_57(self):
        
        teste = Peao.Cria_peao("vermelho", 55)
        
        print("Teste Módulo Peão - Caso de Teste 04 - Peão ultrapassa última casa")
        retorno_esperado = Peao.Move(teste, 5)
        self.assertEqual(retorno_esperado, 1)

    def test_05_mover_peao_zero_casas(self):
        
        teste = Peao.Cria_peao("vermelho", 0)
        
        print("Teste Módulo Peão - Caso de Teste 05 - Dado com número 0")
        retorno_esperado = Peao.Move(teste, 0)
        self.assertEqual(retorno_esperado, -1)
        
    def test_06_mover_peao_casa_negativa(self):
        
        teste = Peao.Cria_peao("vermelho", 0)
        
        print("Teste Módulo Peão - Caso de Teste 06 - Dado com número negativo")
        retorno_esperado = Peao.Move(teste, -2)
        self.assertEqual(retorno_esperado, -1)

    def test_07_mover_peao_casa_acima_6(self):
        
        teste = Peao.Cria_peao("vermelho", 0)
        
        print("Teste Módulo Peão - Caso de Teste 07 - Dado com número acima de 6")
        retorno_esperado = Peao.Move(teste, 8)
        self.assertEqual(retorno_esperado, -1)
        

if __name__ == '__main__':
    unittest.main()

