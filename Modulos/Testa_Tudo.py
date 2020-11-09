from Dados import *
from Tabuleiro import *
from Partida import *
from Peao import *
from Player import *
import unittest
import random

class Testa_Tudo(unittest.TestCase):
    
    def test_01_Cria_dado_vermelho_OK(self):
        teste = Cria_dado("vermelho")

        print("Teste Módulo Dado - Caso de Teste 01 - Criar um elemento dado vermelho")
        retorno_esperado = {"num": None, "sprites": ['../../Assets/Dado_vermelho/dice_1.png',
                    '../../Assets/Dado_vermelho/dice_2.png',
                    '../../Assets/Dado_vermelho/dice_3.png',
                    '../../Assets/Dado_vermelho/dice_4.png',
                    '../../Assets/Dado_vermelho/dice_5.png',
                    '../../Assets/Dado_vermelho/dice_6.png']}
        self.assertEqual(retorno_esperado, teste)

    def test_02_Cria_dado_branco_OK(self):
        teste = Cria_dado("branco")

        print("Teste Módulo Dado - Caso de Teste 02 - Criar um elemento dado branco")
        retorno_esperado = {"num": None, "sprites": ['../../Assets/Dado_branco/dice_1.png',
                    '../../Assets/Dado_branco/dice_2.png',
                    '../../Assets/Dado_branco/dice_3.png',
                    '../../Assets/Dado_branco/dice_4.png',
                    '../../Assets/Dado_branco/dice_5.png',
                    '../../Assets/Dado_branco/dice_6.png']}
        self.assertEqual(retorno_esperado, teste)
        
    def test_03_num_dado_OK(self):
        teste = Cria_dado("vermelho")

        print("Teste Módulo Dado - Caso de Teste 03 - Número do dado está no entre [1,6]")
        retorno_esperado = Clica_dado(teste)
        self.assertEqual(retorno_esperado, 0)

    def test_04_Manda_para_casa_OK(self):
        peao = Cria_peao("branco",5)
        teste =  Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 04 - O peão retorna para a posição 0")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_05_Manda_para_casa_NOK(self):
        peao = ["branco",5]
        teste = Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 06 - O peão não é um dicionário e por isso não volta para posição inicial")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_06_Nao_Captura_Peao_OK(self):
        peao_1 = Cria_peao("branco",5)
        peao_2 = Cria_peao("vermelho",2)
        tabuleiro[5]["peoes"] = [peao_1]
        teste = Captura_peao(peao_1)

        print("Teste Módulo Partida - Caso de Teste 06 - Não há peões para serem capturados nessa casa")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)
        
    def test_07_Captura_Peao_OK(self):
        peao_1 = Cria_peao("branco",1)
        peao_2 = Cria_peao("vermelho",1)
        tabuleiro[1]["peoes"] = [peao_1,peao_2]
        teste = Captura_peao(peao_1)
       
        print("Teste Módulo Partida - Caso de Teste 07 - Peão é capturado com sucesso")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_08_Captura_Peao_NOK(self):
        peao = Cria_peao("branco",59)
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 08 - fin_pos não e um valor válido - MAIOR QUE 57")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_09_Captura_Peao_NOK(self):
        peao = Cria_peao("branco",-1)
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 09 - fin_pos não e um valor válido - MENOR QUE 0")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_10_Captura_Peao_NOK(self):
        peao = {"teste": 2, "modular": 5}
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 10 - fin_pos não existe")
        retorno_esperado = -4
        self.assertEqual(retorno_esperado, teste)

    def test_11_Captura_Peao_NOK(self):
        peao = 1
        teste = Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 11 - Peão não e um dicionário")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_12_Roda_tabuleiro_NOK(self):
        tabuleiro = []
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 12 - Tabuleiro é uma lista vazia")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_13_Roda_tabuleiro_NOK(self):
        casa = {"x": -2, "y": 0, "peoes": [], "semi_torres": [], "torres": []}
        tabuleiro = Cria_tabuleiro(casa,2)
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 13 - Posição da casa em que se encontra é negativa em x")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

    def test_14_Roda_tabuleiro_NOK(self):
        casa = {"x": 0, "y": -5, "peoes": [], "semi_torres": [], "torres": []}
        tabuleiro = Cria_tabuleiro(casa,2)
        teste = Roda_tabuleiro(tabuleiro)
        
        print("Teste Módulo Partida - Caso de Teste 14 - Posição da casa em que se encontra é negativa em y")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)
    

    def test_15_Cria_peao_OK(self):
        
        teste = Cria_peao("branco", 5)

        print("Teste Módulo Peão - Caso de Teste 15 - Criar um peão com sucesso")
        retorno_esperado = {"cor":"branco", "act_pos":5, "fin_pos": 5, "sprite": '../../Assets/peão_branco.png'}
        self.assertEqual(retorno_esperado, teste)
    
    def test_16_mover_peao_OK(self):
        
        teste = Cria_peao("branco", 0)
        
        print("Teste Módulo Peão - Caso de Teste 16 - Mover Peão com sucesso")
        retorno_esperado = Move_peao(teste, 5)
        self.assertEqual(retorno_esperado, 0)
        
    def test_17_mover_peao_casa_57(self):
        
        teste = Cria_peao("branco", 55)
        
        print("Teste Módulo Peão - Caso de Teste 17 - Peão não ultrapassa última casa")
        retorno_esperado = Move_peao(teste, 2)
        self.assertEqual(retorno_esperado, 0)

    def test_18_mover_peao_casa_acima_de_57(self):
        
        teste = Cria_peao("branco", 55)
        
        print("Teste Módulo Peão - Caso de Teste 18 - Peão ultrapassa última casa")
        retorno_esperado = Move_peao(teste, 5)
        self.assertEqual(retorno_esperado, -2)

    def test_19_mover_peao_zero_casas(self):
        
        teste = Cria_peao("branco", 0)
        
        print("Teste Módulo Peão - Caso de Teste 19 - Dado com número 0")
        retorno_esperado = Move_peao(teste, 0)
        self.assertEqual(retorno_esperado, -1)
        
    def test_20_mover_peao_casa_negativa(self):
        
        teste = Cria_peao("branco", 0)
        
        print("Teste Módulo Peão - Caso de Teste 20 - Dado com número negativo")
        retorno_esperado = Move_peao(teste, -2)
        self.assertEqual(retorno_esperado, -1)

    def test_21_mover_peao_casa_acima_6(self):
        
        teste = Cria_peao("branco", 0)
        
        print("Teste Módulo Peão - Caso de Teste 21 - Dado com número acima de 6")
        retorno_esperado = Move_peao(teste, 8)
        self.assertEqual(retorno_esperado, -1)

    def test_22_Cria_tabuleiro_vazio_OK(self):
        
        teste = Cria_tabuleiro_vazio()

        print("Teste Módulo Tabuleiro - Caso de Teste 22 - Criar um tabuleiro com 58 casas vazias ")
        retorno_esperado = []
        for i in range(0,58):
            retorno_esperado.append([])
     
        self.assertEqual(retorno_esperado, teste)
        
    def test_23_Cria_casa_OK(self):
        teste = Cria_casa(10,20)

        print("Teste Módulo Tabuleiro - Caso de Teste 23 - Criar uma casa de tabuleiro com suas coordenadas x e y")
        retorno_esperado = {"x": 10, "y": 20, "peoes": [], "semi_torres": [], "torres": []}
        self.assertEqual(retorno_esperado, teste)

    def test_24_Cria_casa_NOK_falta_x(self):
        teste = Cria_casa(None,20)

        print("Teste Módulo Tabuleiro - Caso de Teste 24 - Falha ao criar casa, valor de x nulo")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)
        
    def test_25_Cria_casa_NOK_falta_y(self):
        teste = Cria_casa(10,None)

        print("Teste Módulo Tabuleiro - Caso de Teste 25 - Falha ao criar casa, valor de y nulo")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)
        
    def test_26_Cria_casa_NOK_falta_xy(self):
        teste = Cria_casa(None,None)

        print("Teste Módulo Tabuleiro - Caso de Teste 26 - Falha ao criar casa, valor de x e y nulos")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_27_Cria_casas_OK_varia_x_positivo(self):
        pos_ini = {"x":5,"y":2}
        teste = Cria_casas(pos_ini,5,2,0,True,False)

        print("Teste Módulo Tabuleiro - Caso de Teste 27 - Cria uma lista de casas do tabuleiro - variando em x - sentido positivo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 7, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 9, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 11, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 13, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)
        
    def test_28_Cria_casas_OK_varia_y_positivo(self):
        pos_ini = {"x":5,"y":2}
        teste = Cria_casas(pos_ini,5,2,0,False,True)
        
        print("Teste Módulo Tabuleiro - Caso de Teste 28 - Cria uma lista de casas do tabuleiro - variando em y - sentido positivo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 4, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 6, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 8, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 10, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)


    def test_29_Cria_casas_OK_varia_x_negativo(self):
        pos_ini = {"x":5,"y":2}
        teste = Cria_casas(pos_ini,5,2,-1,True,False)

        print("Teste Módulo Tabuleiro - Caso de Teste 29 - Cria uma lista de casas do tabuleiro - variando em x - sentido negativo")
        retorno_esperado =  retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 3, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 1, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': -1, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': -3, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)
        
    def test_30_Cria_casas_OK_varia_y_negativo(self):
        pos_ini = {"x":5,"y":2}
        teste = Cria_casas(pos_ini,5,2,-1,False,True)
        
        print("Teste Módulo Tabuleiro - Caso de Teste 30 - Cria uma lista de casas do tabuleiro - variando em y - sentido negativo")
        retorno_esperado = [{'x': 5, 'y': 2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': 0, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -2, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -4, 'peoes': [], 'semi_torres': [], 'torres': []},
                            {'x': 5, 'y': -6, 'peoes': [], 'semi_torres': [], 'torres': []}]
        self.assertEqual(retorno_esperado, teste)

    def test_31_Cria_casas_NOK_varia_xy(self):
        pos_ini = {"x":5,"y":2}
        teste = Cria_casas(pos_ini,5,2,0,True,True)
        
        print("Teste Módulo Tabuleiro - Caso de Teste 31 - Cria uma lista de casas do tabuleiro - variando em x e em y")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

    def test_32_Cria_casas_NOK_sem_xy(self):
        pos_ini = {"x":10,"y":2}
        teste = Cria_casas(pos_ini,5,2,0,False,False)
        
        print("Teste Módulo Tabuleiro - Caso de Teste 32 - Cria uma lista de casas do tabuleiro caso x e y são nulos")
        retorno_esperado = []        
        self.assertEqual(retorno_esperado, teste)

    def test_33_Cria_tabuleiro_OK(self):
        pos_ini = {"x":0,"y":0}
        teste = Cria_tabuleiro(pos_ini,2)

        print("Teste Módulo Tabuleiro - Caso de Teste 33 - Cria todas as casas do tabuleiro")
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

    def test_34_Cria_jogador_OK(self):

        print("Teste Módulo Player - Caso de Teste 34 - Criar um jogador")
        teste = Cria_jogador()  
        retorno_esperado = {"nome": teste["nome"]}
        self.assertEqual(retorno_esperado, teste)

    def test_35_Cria_jogador_NOK_nome_grande(self):
        print("Teste Módulo Player - Caso de Teste 35 - Criar um jogador e ele não escolhe um nome")
        teste = Cria_jogador()
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)


    def test_36_Cria_jogador_NOK_nome_grande(self):
        
        print("Teste Módulo Player - Caso de Teste 36 - Criar um jogador com nome maior que o permitido e entra em loop. Para sair, digitar o nome ou apertar enter")
        teste = Cria_jogador()
        if(teste == -1):
            retorno_esperado = -1
        else:
            retorno_esperado = {"nome": teste["nome"]}
        self.assertEqual(retorno_esperado, teste)

    
    
        

if __name__ == '__main__':
    unittest.main()


