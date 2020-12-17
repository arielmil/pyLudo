from Graphics import *
from Player import *
from Partida import *

global vencedores
vencedores = []

global quantidade_jogadores

DB = Exporta_Conexao()
cursor = db["cursor"]
db = db["db"]

def Quantos_jogam():
    """Permite que o jogador que iniciou o jogo selecione quantos jogadores irão jogar (um inteiro de 2 a 4 (ambos inclusivos) ) (Repete a pergunta até que seja digitado um valor válido, ou sair Sair, ou SAIR (nestes ultimos casos, para a execução do jogo.) ), assim como selecionar as cores que os representam. Entra em um loop para criar a quantidade de jogadores selecionados representados por objetos de Player com seus respectivos nomes. Repete o processo de seleção de cor para um jogador, até que seja digitada uma cor válida, e printa um erro caso o contrário. Mantém-se no loop até que todos os jogadores selecionarem uma cor válida, ou digitem "sair" ou "Sair" ou "SAIR", na seleção de cor ou nome, nesse caso printa uma mensagem adequada e sai do jogo. Retorna um array com um número de índices entre 2 e 4 representando cada jogador, aonde cada índice contém um sub_array tendo em seu primeiro índice um player, e no seu segundo índice um array contendo seus quatro peões já criados e configurados para posição 0, e em seu terceiro índice, um dado da cor que este jogador selecionou."""
    
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
    """Recebe um array contendo em ordem descrescente cronologicamente os jogadores que conseguiram colocar os seus quatro peões na casa 57, e o (único) jogador que não conseguiu por último. Chama a tela de mostrar o vencedor, e de jogar novamente, ou a tela de sair, fornecendo o usuário esta escolha. Independente do escolhido, chama a função Deleta_Informações do módulo Banco_de_dados para encerrar a partida. Sai do jogo caso o usuário selecione sair."""
    
    # Chama as funcoes do graphics para expor os jogadores que acabaram de vencer, e retorna 1
    Deleta_Informacoes(DB)
    
    return 1

def Quem_ganhou(cor, quantidade_jogadores):
    """Deve ser chamada a cada rodada. Recebe uma cor representando o último jogador que jogou, e o número de jogadores jogando e verifica utilizando a função Pega_Posiçoes_Peao_Cor do módulo Banco de Dados se este jogador já possuí todos os seus quatro peões na casa 57. Caso sim, guarda o nome dele em um array (uma variável global) no primeiro índice vazio disponível. Repete o processo até que este array tenha o tamanho de (pessoas jogando - 1). Depois disso coloca o nome do último jogador (o único a não ter os seus quatro peões na casa 57) neste array no primeiro índice vazio disponível. Ao final chama a função Encerrar_jogo passando este array."""
    
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
    """Utilizada junto a função Gerencia_rodada, esta função roda até a partida finalizar."""
    
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
        

def Salvar_XML():
    """Utilizando funções do módulo XML, salva todas as informações da partida que acabou de ser jogada em um arquivo XML. Retorna 0 caso seja bem sucedido, ou -1 caso contrário."""

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
    
jogadores = Quantos_jogam()
Gerencia_rodadas(jogadores)
