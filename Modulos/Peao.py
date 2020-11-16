import pygame
import time

def Cria_peao(cor,ini_pos):
    """ Cria um peão"""
    esse_peao = {"cor":cor, "act_pos":ini_pos, "fin_pos": ini_pos, "sprite": '../Assets/peão'+'_' + cor +'.png'}
    return esse_peao

def Move_peao(peao,numero_dado):
    """Usado para mover um peão"""
    if (numero_dado <= 0 or numero_dado > 6):
            return -1
    if (numero_dado + peao["fin_pos"]) <= 57:
        peao["fin_pos"] = numero_dado + peao["fin_pos"]
        return 0
    else:
        return -2


            
 




            
 



