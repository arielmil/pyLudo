from copy import copy

img = "../../Assets/Board.jpg"

#Não sera exportada.
def Cria_tabuleiro_vazio():
    """Função auxiliar a Cria_tabuleiro."""
    i = 0
    
    tabuleiro = []
    prototipo_casa = []
    
    while (i < 58):
        tabuleiro.append(prototipo_casa)
        i = i + 1

    return tabuleiro

#Ver se sera exportada.
def Cria_casa(x = None, y = None):
    """Cria e retorna um dicionario com dois itens inteiros x e y chamado casa."""
    if (x == None or y == None):
        print("Valor nulo")
        return -1
    casa = {"x": x, "y": y, "peoes": [], "semi_torres": [], "torres": []}
    return casa

#Ver se sera exportada.
def Printa_tabuleiro(tabuleiro):
    """Usada para debugging"""
    i = 1
    while (i < 58):
        print("Posição x da casa: "+  str(i) +": " + str(tabuleiro[i]["x"])+" Posição y da casa "+str(i) + ": " + str(tabuleiro[i]["y"]))
        i = i + 1
    return 0

#Ver se sera exportada.
def Cria_casas (posicao_inicial, times, inc, direction, x = False, y = False):
    """Para ser usado em conjunto com Cria_tabuleiro: Cria uma lista de casas, e as retorna."""
    
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

#Sera exportada.       
def Cria_tabuleiro(posicao_inicial, inc, debugging = False):
    """Chamadada uma vez por tabulerio, cria e preenche um array contendo 58 casas representando as posições no tabuleiro."""
    
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
    '''"Converte" a posicao recebida para a posicao correspondente em relacao as posicoes azuis, para que todas as pecas do jogo de cores distintas possam interagir umas com as outras apesarem de estarem em relacao a sua propria cor em posicoes diferentes. Retorna esta posição convertida em uma váriavel chamada casa_relativa'''
    
    if posicao == 0 or posicao >= 52:
        return posicao
    
    cor_e_defasagem = {'amarelo': 39, 'verde': 26, 'vermelho': 13, 'azul': 0}
    cor = peao["cor"]
    posicao = posicao + cor_e_defasagem[cor]

    if posicao > 52:
        posicao = posicao - 52

    return posicao

def Checa_disponibilidade(numero_dado, casa, cor):
    
    if casa < 0:
        if numero_dado != 6:
            return -1
        return 1

    if casa_relativa + numero_dado > 57:
        return -1
    
    return 1
