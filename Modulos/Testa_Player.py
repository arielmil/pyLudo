from Player import *
import unittest

class Testa_Player(unittest.TestCase):
    
    def test_01_Cria_jogador_OK(self):

        print("Teste Módulo Player - Caso de Teste 01 - Criar um jogador")
        teste = Cria_jogador()  
        retorno_esperado = {"nome": teste["nome"]}
        self.assertEqual(retorno_esperado, teste)

    def test_02_Cria_jogador_NOK_nome_grande(self):
        print("Teste Módulo Player - Caso de Teste 02 - Criar um jogador e ele não escolhe um nome")
        teste = Cria_jogador()
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)


    def test_03_Cria_jogador_NOK_nome_grande(self):
        
        print("Teste Módulo Player - Caso de Teste 03 - Criar um jogador com nome maior que o permitido e entra em loop. Para sair, digitar o nome ou apertar enter")
        teste = Cria_jogador()
        if(teste == -1):
            retorno_esperado = -1
        else:
            retorno_esperado = {"nome": teste["nome"]}
        self.assertEqual(retorno_esperado, teste)
        
if __name__ == '__main__':
    unittest.main()

