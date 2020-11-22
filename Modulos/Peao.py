import pygame
import time

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

def Move_peao(peao,numero_dado):
    """Usado para mover um peão"""
    if (numero_dado <= 0 or numero_dado > 6):
            return -1
    if (numero_dado + peao["fin_pos"]) <= 57:
        peao["fin_pos"] = numero_dado + peao["fin_pos"]
        return 0
    else:
        return -2
