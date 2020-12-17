from Graphics import *
from Player import *
from Partida import *

global vencedores
vencedores = []

global quantidade_jogadores

db = Exporta_Conexao()
cursor = db["cursor"]
db = db["db"]

def Quantos_jogam():
    i = 0
    flag = True
    cores = []
    jogadores = []
    global quantidade_jogadores
    
    while (flag):
        qntJogadores = input("\nPor favor, digite quantos jogadores irão jogar, ou sair, Sair, ou SAIR caso deseje sair do jogo: ")

        if (qntJogadores == "sair" or qntJogadores == "Sair" or qntJogadores == "SAIR"):
            input("\nObrigado por jogar. Pressione enter para sair do jogo.")
            exit()

        elif (qntJogadores not in [2,3,4]):
            print("\nErro: Quantidade de jogadores inválida. Por favor, tente novamente.")

        else:
            flag = False

    for i in range(0, qntJogadores):
        
        flag = True
        jogador = Cria_jogador()

        while (flag):
            cor = input("\nPor favor, escolha a sua cor, ou sair, Sair, ou SAIR caso deseje sair do jogo: ")

            if (cor == "sair" or cor == "Sair" or cor == "SAIR"):
                input("\nObrigado por jogar. Pressione enter para sair do jogo.")
                exit()

            elif (cor not in ["amarelo", "azul", "verde", "vermelho"]):
                print("\nErro: Cor inválida. Por favor, tente novamente.")

            elif cor in cores:
                print("\nErro: Essa cor já foi escolhida. Por favor escolha outra cor.")
            
            else:
                cores.append(cor)
                peoes = Cria_peoes(cor)
                dado = Cria_dado(cor)
                jogadores.append([jogador, peoes, cor])
                flag = False
    
    quantidade_jogadores = len(jogadores)
    return jogadores

def Encerrar_jogo(vencedores):
    # Chama as funcoes do graphics para expor os jogadores que acabaram de vencer, e retorna 1
    return 1

def Quem_ganhou(cor, quantidade_jogadores):
    checagem = Pega_Posicoes_Peao_cor(cursor, cor)
    
    if checagem == [57, 57, 57, 57]:
        for jogador in jogadores:

            # Encontra o nome do jogador pela cor representando-o no jogo, e encontra esta cor pelos peoes dele
            if jogador[1][0]["cor"] == cor:
                vencedores.append({"nome": jogador[0]["nome"], cor: cor)}
                
    if len(vencedores) == quantidade_jogadores - 1:
        return Encerrar_jogo(vencedores)
        
    return 0
    
def Gerencia_rodadas(jogadores):

    encerrado = 0
    i = -1
    
    while !encerrado:

        i = i + 1
        
        if i >= quantidade_jogadores - 1:
    	    i = -1
    	    continue
    	
    	jogador = jogadores[i]
    	nome = jogador[0]["nome"]
    	peoes = jogador[1]
    	cor = peoes[0]["cor"]
    	dado = jogador[2]
    	
    	for vencedor in vencedores:
    	    if cor == vencedor["cor"]:
    	        continue
    	    
    	casa_clicada = Clica_casa()
    	
    	checa = Checa_peao(jogador, casa_clicada, numero_dado)
    	
    	while checa < 0:
    	    checa = Checa_peao(jogador, casa_clicada, numero_dado)
    	
    	num_peao = checa
    	peao = peoes[num_peao]
    	
    	Gerencia_rodada(peao, casa_clicada, dado)
    	
    	encerrado = Quem_ganhou(cor, quantidade_jogadores)
    	   	
    return 0
    
jogadores = Quantos_jogam()
Gerencia_rodadas(jogadores)
