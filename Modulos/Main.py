#from Banco_de_dados import *
from Graphics import *
from Player import *
from Partida import *
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

def Quantos_jogam():
    i = 0
    flag = True
    cores = []
    jogadores = []
    
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
                jogadores.append([jogador, peoes])
                flag = False

    return jogadores

def Cria_dados(jogadores):
    dados = []
    for jogador in jogadores:
        cor = jogador[1]["cor"]
        dado = Cria_dado(cor)
        dados.append(dado)

    return dados
        

def Salvar_XML():
    titulo = Element('Título')
    titulo.text = 'Ludo: Grupo 1'
    historico = Element('Histórico')
    rodada = SubElement(historico, 'Rodada')
    rodada.text = '1'
    localizacao = SubElement(historico, 'Localização dos peões')
    azul = SubElement(localizacao, 'Azul')
    vermelho = SubElemente(localizacao, 'Vermelho')
    verde = SubElement(localizacao, 'Verde')
    amarelo = SubElement(localizacao, 'Amarelo')
    cores = [azul, vermelho, verde, amarelo]
    posicoes_iniciais = [(330, 522), (285, 85), (725, 30), (770, 478)]
    for i in range(len(cores)):
        peao1 = SubElement(cores[i], 'Peão1')
        peao2 = SubElement(cores[i], 'Peão2')
        peao3 = SubElement(cores[i], 'Peão3')
        peao4 = SubElement(cores[i], 'Peão4')
    nome_arquivo = 'Salva_XML.xml'
    with open(nome_arquivo, 'w') as file_object:
        file_object.write(Formata_saida(historico))

