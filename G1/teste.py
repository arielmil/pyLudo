import unittest
from Usuario import *

class Testa_vacina_app(unittest.TestCase):

    def test_01_Cria_usuario_NOK_nao_escolheu_nome_deixou_em_branco(self):
        print("Caso de Teste 01 - Cria um usuário e ele não escolhe um nome, pois o usuário optou por deixar em branco.")
        teste = Cria_usuario()
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_02_Cria_usuario_NOK_nao_escolheu_nome_tentativas_acabaram(self):
        print("Caso de Teste 02 - Cria um usuário e ele não escolhe um nome, pois suas tentativas acabaram.")
        teste = Cria_usuario()
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

    def test_03_Cria_usuario_NOK_nao_escolheu_senha_deixou_em_branco(self):
        print("Caso de Teste 03 - Cria um usuário e ele não escolhe uma senha, pois ele optou por deixar em branco.")
        teste = Cria_usuario()
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_04_Cria_usuario_NOK_nao_escolheu_senha_tentativas_acabaram(self):
        print("Caso de Teste 04 - Cria um usuário e ele não escolhe uma senha, pois suas tentativas acabaram.")
        teste = Cria_usuario()
        retorno_esperado = -4
        self.assertEqual(retorno_esperado, teste)

    def test_05_Cria_usuario_OK(self):
        print("Caso de Teste 05 - Cria um usuário com sucesso.")
        teste = Cria_usuario()
        retorno_esperado = {"nome": teste["nome"], "senha": teste["senha"]}
        self.assertEqual(retorno_esperado, teste)
        
if __name__ == '__main__':
    unittest.main()
