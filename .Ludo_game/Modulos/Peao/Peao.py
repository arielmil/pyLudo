import pygame
import time

def Inicializa_peao(cor,ini_pos):
    esse_peao = {"cor":cor, "act_pos":ini_pos, "fin_pos": ini_pos, "sprite": '../../Assets/peão'+'_' + cor +'.png'}
    return esse_peao

def Move_peao(peao,numero_dado):
    '''Usado para mover um peão'''
    if (numero_dado <= 0 or numero_dado > 6):
            return -1
    if (numero_dado + peao["fin_pos"]) <= 57:
        peao["fin_pos"] = numero_dado + peao["fin_pos"]
        return 0
    else:
        return -2

'''def Desenha_peao(peao):
    if peao["act_pos"] == peao["fin_pos"]:
        x,y = get_pos(peao["act_pos"])
        screen.blit(peao["sprite"], (x, y))
        
    else:
        x_ini,y_ini = get_pos(peao["act_pos"])
        x_fin,y_fin = get_pos(peao["fin_pos"])
        
        screen.blit(peao["sprite"], (x_ini, y_ini))
        if x_ini < x_fin:
            x_ini += 1
        elif  x_ini > x_fin:
            x_ini -= 1
        if y_ini < y_fin:
            y_ini += 1
        elif  y_ini > y_fin:
            y_ini -= 1

        x_prox,y_prox = get_pos(peao["act_pos"]+1)
        if x_prox == x_ini and y_prox == y_ini:
            peao["act_pos"] += 1
            time.sleep(1.4)'''
            
 




            
 



