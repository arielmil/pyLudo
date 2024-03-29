from copy import copy

img = "../../Assets/Board.jpg"

def Cria_tabuleiro_vazio():
    """Utilizado pela função Cria_tabuleiro, esta função cria e retorna um array de 58 índices com todos os valores de seus índices iguais a [] (lista vazia)."""
    i = 0
    
    tabuleiro = []
    prototipo_casa = []
    
    while (i < 58):
        tabuleiro.append(prototipo_casa)
        i = i + 1

    return tabuleiro

def Cria_casa(x = None, y = None):
    """Recebe como parâmetro um ou dois valores inteiros (x e y). Cria e retorna um dicionario chamado Casa representando uma casa do tabuleiro com suas coordenadas x e y iguais aos parametros recebidos, além de que Casa terá também os campos: "peoes" (uma lista que mantem registro dos peões nessa casa), "semi_torres" (uma lista que mantem registro das semi torres nessa casa), e "torres" (uma lista que mantem registro das torres nessa casa), todos iguais a [] (lista vazia). Retorna -1 e printa uma mensagem de erro caso não sejam recebidos x e y."""
    
    if (x == None or y == None):
        print("Valor nulo")
        return -1
    casa = {"x": x, "y": y, "peoes": [], "semi_torres": [], "torres": []}
    return casa

def Printa_tabuleiro(tabuleiro):
    """Usados para fins de debug. Recebe um tabuleiro (um array de 58 casas) e printa todas as coordenadas x e y de cada uma das casas de forma estruturada."""
    
    i = 1
    while (i < 58):
        print("Posição x da casa: "+  str(i) +": " + str(tabuleiro[i]["x"])+" Posição y da casa "+str(i) + ": " + str(tabuleiro[i]["y"]))
        i = i + 1

def Cria_casas (posicao_inicial, times, inc, direction, x = False, y = False):
    """Recebe como parâmetros: Uma casa como posição inicial, o número de casas que irá criar, a distância em x ou y entre duas casas, a direção e o sentido que irá seguir. Utilizando a função Cria_Casa, esta função cria com seus valores x ou y sequencialmente uma ou mais casas, seguindo pela direção (vertical ou horizontal) e pelo sentido  (negativo se igual a -1 , e positivo caso o contrário). Retorna um array de casas, ou -1 em caso de erro."""
        
    i = 0
    j = 0
    
    casas_array = []
    
    casa = None
    
    if (x == True and y == True):
    	print("Erro, x e y são True.")
    	return -2
    
    if (x):
        if (direction != -1):
            while (i < times):
                casa = Cria_casa(posicao_inicial["x"] + j, posicao_inicial["y"])
                if (type(casa) == dict):
                    casas_array.append(casa)
                    i = i + 1
                    j = inc * i
                else:
                    print("Erro na função Cria_casa: Valor retornado por ela não é um dicionario.")
                    return -1

        else:
            while (i < times):
                casa = Cria_casa(posicao_inicial["x"] - j, posicao_inicial["y"])
                if (type(casa) == dict):
                    casas_array.append(casa)
                    i = i + 1
                    j = inc * i
                else:
                    print("Erro na função Cria_casa: Valor retornado por ela não é um dicionario.")
                    return -1  
    elif(y):
        if (direction != -1):
            while (i < times):
                casa = Cria_casa(posicao_inicial["x"], posicao_inicial["y"] + j)
                if (type(casa) == dict):
                    casas_array.append(casa)
                    i = i + 1
                    j = inc * i
                else:
                    print("Erro na função Cria_casa: Valor retornado por ela não é um dicionario.")
                    return -1

        else:
            while (i < times):
                casa = Cria_casa(posicao_inicial["x"], posicao_inicial["y"] - j)
                if (type(casa) == dict):
                    casas_array.append(casa)
                    i = i + 1
                    j = inc * i
                else:
                    print("Erro na função Cria_casa: Valor retornado por ela não é um dicionario.")
                    return -1
        
    return casas_array

def Cria_tabuleiro(posicao_inicial, inc, debugging = False):
    """Recebe como parâmetros: Uma casa como posição inicial, e a distancia em x ou y entre duas casas, além de um parametro opcional booleano chamado debugging. Cria utilizando sequencialmente a função Cria_Casas todas as casas necessárias para o tabuleiro poder ser usado com seus valores x e y. Retorna um array de 58 Casas representando o tabuleiro. Caso debugging seja diferente de False, printa utilizando a função Printa_tabuleiro todas as casas do tabuleiro criado."""    
    times = 5

    tabuleiro = Cria_tabuleiro_vazio()
    
    #tabuleiro[0] = Posição aonde o jogador precisa tirar 0 para se mover !!


    #Posições 1 a 5:
    tabuleiro[1:6] = Cria_casas(posicao_inicial, times, inc, 1, False, True)

    #Diagonal:
    posicao_inicial["x"] = (tabuleiro[5])["x"] - inc
    posicao_inicial["y"] = (tabuleiro[5])["y"] + inc

    times = 6


    #Posições 6 a 11:
    tabuleiro[6:12] = Cria_casas(posicao_inicial, times, inc, -1, True, False)

    posicao_inicial["x"] = (tabuleiro[11])["x"]
    posicao_inicial["y"] = (tabuleiro[11])["y"] + inc
 
    ###posicao_inicial["x"] = p

    times = 2


    #Posições 12 a 13:
    tabuleiro[12:14] = Cria_casas(posicao_inicial, times, inc, 1, False, True)

    posicao_inicial["x"] = (tabuleiro[13])["x"] + inc
    posicao_inicial["y"] = (tabuleiro[13])["y"]
    
    times = 5


    #Posições 14 a 18:
    tabuleiro[14:19] = Cria_casas(posicao_inicial, times, inc, 1, True, False)

    #Diagonal:
    posicao_inicial["x"] = (tabuleiro[18])["x"] + inc
    posicao_inicial["y"] = (tabuleiro[18])["y"] + inc

    times = 6


    #Posições 19 a 24:
    tabuleiro[19:25] = Cria_casas(posicao_inicial, times, inc, 1, False, True)

    posicao_inicial["x"] = (tabuleiro[24])["x"] + inc
    posicao_inicial["y"] = (tabuleiro[24])["y"]
    
    times = 2


    #Posições 25 a 26:
    tabuleiro[25:27] = Cria_casas(posicao_inicial, times, inc, 1, True, False)

    posicao_inicial["x"] = (tabuleiro[26])["x"]
    posicao_inicial["y"] = (tabuleiro[26])["y"] - inc
    
    times = 5


    #Posições 27 a 31:
    tabuleiro[27:32] = Cria_casas(posicao_inicial, times, inc, -1, False, True)

    #Diagonal:
    posicao_inicial["x"] = (tabuleiro[31])["x"] + inc
    posicao_inicial["y"] = (tabuleiro[31])["y"] - inc

    times = 6


    #Posições 32 a 37:
    tabuleiro[32:38] = Cria_casas(posicao_inicial, times, inc, 1, True, False)

    posicao_inicial["x"] = (tabuleiro[37])["x"]
    posicao_inicial["y"] = (tabuleiro[37])["y"] - inc
    
    times = 2


    #Posições 38 a 39:
    tabuleiro[38:40] = Cria_casas(posicao_inicial, times, inc, -1, False, True)

    posicao_inicial["x"] = (tabuleiro[39])["x"] - inc
    posicao_inicial["y"] = (tabuleiro[39])["y"]
    
    times = 5


    #Posições 40 a 44:
    tabuleiro[40:45] = Cria_casas(posicao_inicial, times, inc, -1, True, False)

    #Diagonal:
    posicao_inicial["x"] = (tabuleiro[44])["x"] - inc
    posicao_inicial["y"] = (tabuleiro[44])["y"] - inc

    times = 6


    #Posições 45 a 50:
    tabuleiro[45:51] = Cria_casas(posicao_inicial, times, inc, -1, False, True)

    posicao_inicial["x"] = (tabuleiro[50])["x"] - inc
    posicao_inicial["y"] = (tabuleiro[50])["y"]
    
    times = 1

    #Posição 51:
    tabuleiro[51] = Cria_casa(tabuleiro[50]["x"] - inc, tabuleiro[50]["y"])

    posicao_inicial["x"] = (tabuleiro[51])["x"]
    posicao_inicial["y"] = (tabuleiro[51])["y"] + inc

    times = 6

    #Posições 52 a final (57):
    tabuleiro[52:58] = Cria_casas(posicao_inicial, times, inc, 1, False, True)

    if debugging:
        Printa_tabuleiro(tabuleiro)

    return tabuleiro

def Converte_posicao(cor, posicao):
    '''Recebe um inteiro representando uma posição (número de casa) do tabuleiro, e uma cor, "converte" a posicao recebida para a posicao correspondente em relacao as posicoes azuis, para que todas as pecas do jogo de cores distintas possam interagir umas com as outras apesarem de estarem em relacao a sua propria cor em posicoes diferentes. Retorna esta posição convertida em uma váriavel chamada casa_relativa.'''
    
    if posicao == 0 or (posicao >= 52 and posicao <= 57):
        return posicao

    elif posicao >= 58:
        return -1
    
    cor_e_defasagem = {'amarelo': 39, 'verde': 26, 'vermelho': 13, 'azul': 0}
    cor = peao["cor"]
    posicao = posicao + cor_e_defasagem[cor]

    if posicao > 52:
        posicao = posicao - 52

    return posicao

def Checa_disponibilidade(casa, cor):
    """Recebe dois valores inteiros um representando o número do dado que acabou de ser tirado, e o outro representando uma posicao (número de casa) e uma cor. Assumindo que um peão da cor recebida exista nessa casa, checa se ele pode se mover baseado no número de dado que tirou. Retorna -1 caso esse peão não possa se movimentar, ou 1 caso ele possa se movimentar. OBS: Convenciona-se que as casas iniciais de cada peão (antes da casa 1) sejam representadas por números negativos de -1 a -4 (ambos inclusos)."""

    if casa < 0 or casa > 57:
        return -1
    
    return 1
    
__all__ = ['Cria_tabuleiro', 'Converte_posicao', 'Checa_disponibilidade']
