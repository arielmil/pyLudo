import random
import pygame
import time

def Cria_dado(cor):
    esse_dado = {"num": None, "sprites": ['../../Assets/Dado_'+cor+'/dice_1.png',
                    '../../Assets/Dado_'+cor+'/dice_2.png',
                    '../../Assets/Dado_'+cor+'/dice_3.png',
                    '../../Assets/Dado_'+cor+'/dice_4.png',
                    '../../Assets/Dado_'+cor+'/dice_5.png',
                    '../../Assets/Dado_'+cor+'/dice_6.png']}
    return esse_dado

def Joga_dado(dado):
    '''Gera um número randomico entre [1,6]'''
    dado["num"] = random.randint(1,6)
    return 0

'''def Animacao_dado(self,num_dado,tempo_movimento_peao):
  ''''''Faz a animação do dado''''''
    x,y = Aonde_clicou() #posição em que o dado fica
    x_margem_menor = 0.9*x #margem de erro inferior
    x_margem_maior = 1.1*x #margem de erro superior
    y_margem_menor = 0.9*y #margem de erro inferior
    y_margem_maior = 1.1*y #margem de erro superior
    texto_erro_clique = font.render('CLIQUE NO DADO',True,black)
    texto_erro_dado = font.render('NÚMERO DO DADO INCORRETO',True, black)
    
    if (x in range(x_margem_menor,x_margem_maior) and y in range(y_margem_menor,y_margem_maior)):
        
        
       while cont != 10:
            face = random.randit(0,5)
            screen.blit(self.sprite[face])
            cont += 1
            time.sleep(0.1)
        
        for i in range(tempo_movimento_peao):
            screen.blit(self.sprite[num_dado - 1])         
            time.sleep(1)
        sreen.fill(white) #depois de o peão se movimentar até a casa desejada, o valor do dado é apagado
        
    else:
        screen.blit(texto_erro_clique,(250,250))'''

