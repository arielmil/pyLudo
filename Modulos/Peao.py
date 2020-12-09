def Cria_peao(cor, pos):
    """ Cria um peão"""
    esse_peao = {"cor":cor, "pos": pos, "sprite": '../Assets/peão'+'_' + cor +'.png'}
    return esse_peao

def Cria_peoes(cor):
    peoes = []
    #Tratar aqui as quatro posicoes iniciais para as 4 cores diferentes.
    for i in range(0,4):
        peoes.append(Cria_peao(cor,0))
    return peoes

def Move (peao,numero_dado):
    """Usado para mover um peão"""
    if (numero_dado <= 0 or numero_dado > 6):
        print("\nNumero de dado recebido invalido.")
        return -1
    if (numero_dado + peao["pos"]) <= 57:
        peao["pos"] = numero_dado + peao["pos"]
        return 0
    else:
        #Peao nao pode se mover.
        return 1
