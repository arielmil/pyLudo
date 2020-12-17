import Tabuleiro 
import unittest

'''Arquivo de testes do módulo Tabuleiro'''

class Testa_Tabuleiro(unittest.TestCase):

    def test_01_Cria_tabuleiro_vazio_OK(self):
        
        teste = Tabuleiro.Cria_tabuleiro_vazio()

        print("\nTeste Módulo Tabuleiro - Caso de Teste 01 - Criar um tabuleiro com 58 casas vazias ")
        retorno_esperado = []
        for i in range(0,58):
            retorno_esperado.append([])
     
        self.assertEqual(retorno_esperado, teste)
        
    def test_02_Cria_casa_OK(self):
        teste = Tabuleiro.Cria_casa(10,20)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 02 - Criar uma casa de tabuleiro com suas coordenadas x e y")
        retorno_esperado = {"x": 10, "y": 20, "peoes": [], "semi_torres": [], "torres": []}
        self.assertEqual(retorno_esperado, teste)

    def test_03_Cria_casa_NOK_falta_x(self):
        teste = Tabuleiro.Cria_casa(None,20)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 03 - Falha ao criar casa, valor de x nulo")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)
        
    def test_04_Cria_casa_NOK_falta_y(self):
        teste = Tabuleiro.Cria_casa(10,None)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 04 - Falha ao criar casa, valor de y nulo")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)
        
    def test_05_Cria_casa_NOK_falta_xy(self):
        teste = Tabuleiro.Cria_casa(None,None)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 05 - Falha ao criar casa, valor de x e y nulos")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_06_Cria_casas_OK_varia_x_positivo(self):
        pos_ini = {"x":5,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,0,True,False)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 06 - Cria uma lista de casas do tabuleiro - variando em x - sentido positivo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 7, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 9, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 11, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 13, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)
        
    def test_07_Cria_casas_OK_varia_y_positivo(self):
        pos_ini = {"x":5,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,0,False,True)
        
        print("\nTeste Módulo Tabuleiro - Caso de Teste 07 - Cria uma lista de casas do tabuleiro - variando em y - sentido positivo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 4, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 6, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 8, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)


    def test_08_Cria_casas_OK_varia_x_negativo(self):
        pos_ini = {"x":5,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,-1,True,False)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 08 - Cria uma lista de casas do tabuleiro - variando em x - sentido negativo")
        retorno_esperado =  retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 3, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 1, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': -1, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': -3, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)
        
    def test_09_Cria_casas_OK_varia_y_negativo(self):
        pos_ini = {"x":5,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,-1,False,True)
        
        print("\nTeste Módulo Tabuleiro - Caso de Teste 09 - Cria uma lista de casas do tabuleiro - variando em y - sentido negativo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 0, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -4, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -6, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)

    def test_10_Cria_casas_NOK_varia_xy(self):
        pos_ini = {"x":5,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,0,True,True)
        
        print("\nTeste Módulo Tabuleiro - Caso de Teste 10 - Cria uma lista de casas do tabuleiro - variando em x e em y")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

    def test_11_Cria_casas_NOK_sem_xy(self):
        pos_ini = {"x":10,"y":2}
        teste = Tabuleiro.Cria_casas(pos_ini,5,2,0,False,False)
        
        print("\nTeste Módulo Tabuleiro - Caso de Teste 11 - Cria uma lista de casas do tabuleiro caso x e y são nulos")
        retorno_esperado = []        
        self.assertEqual(retorno_esperado, teste)

    def test_12_Cria_tabuleiro_OK(self):
        pos_ini = {"x":0,"y":0}
        teste = Tabuleiro.Cria_tabuleiro(pos_ini,2)

        print("\nTeste Módulo Tabuleiro - Caso de Teste 12 - Cria todas as casas do tabuleiro")
        retorno_esperado = [{'x': 0, 'y': 0, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 0, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 0, 'y': 4, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 0, 'y': 6, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 0, 'y': 8, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -2, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -4, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -6, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -8, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -10, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -12, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -12, 'y': 12, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -12, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -10, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -8, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -6, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': -4, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': -2, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 0, 'y': 16, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 0, 'y': 18, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 0, 'y': 20, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 0, 'y': 22, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 0, 'y': 24, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 0, 'y': 26, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 2, 'y': 26, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': 26, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 24, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': 22, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 20, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': 18, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 16, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 6, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 8, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 10, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 12, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 14, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 16, 'y': 14, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 16, 'y': 12, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 16, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 14, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 12, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 10, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 8, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 6, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 8, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': 6, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 4, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 4, 'y': 0, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 4, 'y': -2, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 2, 'y': -2, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 2, 'y': 0, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 2, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 2, 'y': 4, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 2, 'y': 6, 'peoes': [], 'semi_torres': [], 'torres': []}, {'x': 2, 'y': 8, 'peoes': [], 'semi_torres': [], 'torres': []}, 
                            {'x': 2, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste[1:])

    def test_13_Converte_posicao_OK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 13 - Converte_posicao com posicao = 0 funcionando com sucesso.")
        
        cor = "vermelho"
        posicao = 0
        
        teste = Tabuleiro.Converte_posicao(cor, posicao)
        retorno_esperado = posicao

        self.assertEqual(retorno_esperado, teste)
        
    def test_14_Converte_posicao_OK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 14 -  Converte_posicao com posicao = 52 funcionando com sucesso.")

        cor = "vermelho"
        posicao = 52
        
        teste = Tabuleiro.Converte_posicao(cor, posicao)
        retorno_esperado = posicao

        self.assertEqual(retorno_esperado, teste)

    def test_15_Converte_posicao_OK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 15 - Converte_posicao com posicao = 54 funcionando com sucesso.")

        cor = "vermelho"
        posicao = 54
        
        teste = Tabuleiro.Converte_posicao(cor, posicao)
        retorno_esperado = posicao

        self.assertEqual(retorno_esperado, teste)

    def test_16_Converte_posicao_NOK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 16 - Converte_posicao falhando por posicao > 57.")

        cor = "vermelho"
        posicao = 58
        
        teste = Tabuleiro.Converte_posicao(cor, posicao)
        retorno_esperado = -1

        self.assertEqual(retorno_esperado, teste)
        
    def test_17_Checa_disponibilidade_OK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 17 - Checa_disponibilidade funcionando com sucesso.")

        cor = "vermelho"

        teste = Tabuleiro.Checa_disponibilidade(57, cor)
        retorno_esperado = 1
        
        self.assertEqual(retorno_esperado, teste)
        
    def test_18_Checa_disponibilidade_NOK(self):
        print("\nTeste Modulo Tabuleiro - Caso de Teste 18 - Checa_disponibilidade falhando por posicao >= 58.")

        cor = "vermelho"

        teste = Tabuleiro.Checa_disponibilidade(58, cor)
        retorno_esperado = -1

        self.assertEqual(retorno_esperado, teste)
        
if __name__ == '__main__':
    unittest.main()

