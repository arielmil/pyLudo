import pygame
import time
    
 def Inicia_telas():
    """Inicia e renderiza a interface gráfica"""
    return 0
    
def Desenha_jogo():
    """Renderiza as imagens recebidas"""
    return 0
    
def Aonde_clicou():
    """Identifica em que lugar da tela foi clicado"""
    return 0

def Renderiza_tela_quantos_jogam():
    """Permite selecionar quantos jogadores irão participar da partida"""
    return 0

def Desenha_peao():
    """Desenha a movimentação do peão"""
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
            time.sleep(1.4)

def Desenha_tabuleiro():
    """Implementa a funcionalidade necessária para desenhar o tabuleiro"""
    return 0

def Desenha_dado():
    """Implementa a funcionalidade necessária para desenhar o dado."""
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
        screen.blit(texto_erro_clique,(250,250))
        
        
 
'''BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139,69,19)

screen = pygame.display.set_mode((1080, 720))
icon = pygame.image.load('Assets/icone_ludo.png')
pygame.display.set_caption('Ludo games')
pygame.display.set_icon(icon)

pygame.init()

player_1 = player('Vermelho')
player_2 = player('Amarelo')
player_3 = player('Azul')
player_4 = player('Roxo')

tabuleiro = Tabuleiro(player_1, player_2, player_3, player_4)

running = True
while running:
    screen.fill(BROWN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tabuleiro.draw()
    pygame.display.update()'''