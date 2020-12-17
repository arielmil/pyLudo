import Partida
import Peao
import Dados
import Tabuleiro
import unittest

casa = {"x": 0, "y": 0, "peoes": [], "semi_torres": [], "torres": []}
MENOR_CASA = 0
MAIOR_CASA = 57
tabuleiro = Tabuleiro.Cria_tabuleiro(casa,2)
ALT_TABULEIRO = 20
LARG_CASA = 25

dado = Dados.Cria_dado('Vermelho')

'''Arquivo de testes do módulo Partida'''

class Testa_Partida(unittest.TestCase):
    
    def test_01_Manda_para_casa_OK(self):
        peao = Peao.Cria_peao("branco",5)
        teste = Partida.Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 01 - O peão retorna para a posição 0")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_02_Manda_para_casa_NOK(self):
        peao = ["branco",5]
        teste = Partida.Manda_para_casa(peao)

        print("Teste Módulo Partida - Caso de Teste 02 - O peão não é um dicionário e por isso não volta para posição inicial")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_03_Nao_Captura_Peao_OK(self):
        peao_1 = Peao.Cria_peao("branco",5)
        peao_2 = Peao.Cria_peao("vermelho",2)
        tabuleiro[5]["peoes"] = [peao_1]
        teste = Partida.Captura_peao(peao_1)

        print("Teste Módulo Partida - Caso de Teste 03 - Não há peões para serem capturados nessa casa")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)
        
    def test_04_Captura_Peao_OK(self):
        peao_1 = Peao.Cria_peao("branco",1)
        peao_2 = Peao.Cria_peao("vermelho",1)
        tabuleiro[1]["peoes"] = [peao_1,peao_2]
        teste = Partida.Captura_peao(peao_1)
       
        print("Teste Módulo Partida - Caso de Teste 04 - Peão é capturado com sucesso")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_05_Captura_Peao_NOK(self):
        peao = Peao.Cria_peao("branco",59)
        teste = Partida.Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 05 - fin_pos não e um valor válido - MAIOR QUE 57")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_06_Captura_Peao_NOK(self):
        peao = Peao.Cria_peao("branco",-1)
        teste = Partida.Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 06 - fin_pos não e um valor válido - MENOR QUE 0")
        retorno_esperado = -3
        self.assertEqual(retorno_esperado, teste)

    def test_07_Captura_Peao_NOK(self):
        peao = {"teste": 2, "modular": 5}
        teste = Partida.Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 07 - fin_pos não existe")
        retorno_esperado = -4
        self.assertEqual(retorno_esperado, teste)

    def test_08_Captura_Peao_NOK(self):
        peao = 1
        teste = Partida.Captura_peao(peao)
       
        print("Teste Módulo Partida - Caso de Teste 08 - Peão não e um dicionário")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_09_Manda_para_casa_OK(self):
        peao = Peao.Cria_peao("branco", 1)
        teste = Partida.Manda_para_casa(peao)
       
        print("Teste Módulo Partida - Caso de Teste 09 - Manda para casa com sucesso")
        retorno_esperado = 0
        self.assertEqual(retorno_esperado, teste)

    def test_10_Manda_para_casa_NOK(self):
        peao = Peao.Cria_peao("branco", 110)
        teste = Partida.Manda_para_casa(peao)
       
        print("Teste Módulo Partida - Caso de Teste 09 - fin_pos não é um valor válido - MAIOR QUE 57")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_11_Manda_para_casa_NOK(self):
        peao = 'a'
        teste = Partida.Manda_para_casa(peao)
       
        print("Teste Módulo Partida - Caso de Teste 11 - Peão não é um dicionário")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_12_Checa_disponibilidade_peao_NOK(self):
        peao = Peao.Cria_peao("vermelho", 5, 0)
        teste = Partida.Checa_disponibilidade(peao)
       
        print("Teste Módulo Partida - Caso de Teste 12 - Checa disponibilidade com erro: Peão está na posição recebida, mas não pode andar")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_13_Checa_disponibilidade_peao_OK(self):
        teste = Partida.Manda_para_casa("azul", 6, 0)
       
        print("Teste Módulo Partida - Caso de Teste 13 - Checa disponibilidade com sucesso: Peão está na posição recebida, e pode andar")
        retorno_esperado = 1
        self.assertEqual(retorno_esperado, teste)

    def test_14_Checa_disponibilidade_peao_NOK(self):
        teste = Partida.Checa_disponibilidade_peao("amarelo", 5, 54)
       
        print("Teste Módulo Partida - Caso de Teste 14 -Checa disponibilidade com erro: Peão está na posição recebida, mas não pode andar")
        retorno_esperado = -1
        self.assertEqual(retorno_esperado, teste)

    def test_15_Checa_disponibilidade_peao_OK(self):
        teste = Partida.Checa_disponibilidade_peao("amarelo", 3, 54)
       
        print("Teste Módulo Partida - Caso de Teste 15 - Checa disponibilidade com sucesso: Peão está na posição recebida, e pode andar")
        retorno_esperado = 1
        self.assertEqual(retorno_esperado, teste)

    def test_16_Checa_peao_NOK(self):
        jogador = Cria_jogador(1)
        teste = Partida.Checa_peao(jogador, 12, 2)
        checa = Checa_disponibilidade_peao("amarelo", 5, 54)
       
        print("Teste Módulo Partida - Caso de Teste 16 - Checa_peao com erro: peão não pode andar.")
        retorno_esperado = checa
        self.assertEqual(retorno_esperado, teste)

    def test_17_Checa_peao_OK(self):
        jogador = Cria_jogador(1)
        teste = Partida.Checa_peao(jogador, 12, 2)
        checa = Checa_disponibilidade_peao("amarelo", 2, 10)
       
        print("Teste Módulo Partida - Caso de Teste 17 - Checa_peao com sucesso.")
        retorno_esperado = 2 #num
        self.assertEqual(retorno_esperado, teste)

    def test_18_Checa_peao_NOK(self):
        jogador = Cria_jogador(1)
        teste = Partida.Checa_peao(jogador, 12, 2)
        checa = Checa_disponibilidade_peao("amarelo", 2, 8)
       
        print("Teste Módulo Partida - Caso de Teste 17 - Checa_peao com erro: Nenhum peão válido foi selecionado.")
        retorno_esperado = -2
        self.assertEqual(retorno_esperado, teste)

        
if __name__ == '__main__':
    unittest.main()

