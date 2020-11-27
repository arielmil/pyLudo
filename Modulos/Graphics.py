import pygame
from pygame.locals import *
import time
from random import randint

def Inicia_telas():
    """Inicia e renderiza a interface gráfica"""
    return 0


def Desenha_jogo():
    """Renderiza as imagens recebidas"""
    imagens = []
    tabuleiro = pygame.image.load(path+'Tabuleiro.png')
    peao_vermelho = pygame.image.load(path + 'peão_vermelho.png')
    peao_verde = pygame.image.load(path + 'peão_verde.png')
    peao_azul = pygame.image.load(path + 'peão_azul.png')
    peao_amarelo = pygame.image.load(path + 'peão_amarelo.png')
    imagens = [tabuleiro, [peao_vermelho, peao_verde, peao_azul, peao_amarelo]]
    return imagens
   
def Aonde_clicou():
    """Identifica em que lugar da tela foi clicado"""
    onde = 0
    if pygame.mouse.get_pressed() == (1,0,0):
        onde = pygame.mouse.get_pos()
       
    return onde

def Renderiza_tela_quantos_jogam():
    """Permite selecionar quantos jogadores irão participar da partida"""
    return 0

def Desenha_peao(img_peao):
    """Desenha a movimentação do peão"""
    #Peões vermelhos
    tela.blit(img_peao[0], (330, 70))
    tela.blit(img_peao[0], (250, 140))
    tela.blit(img_peao[0], (400, 140))
    tela.blit(img_peao[0], (330, 210))

    #Peões verdes
    tela.blit(img_peao[1], (725, 60))
    tela.blit(img_peao[1], (655, 140))
    tela.blit(img_peao[1], (795, 140))
    tela.blit(img_peao[1], (725, 210))

    #Peões azuis
    tela.blit(img_peao[2], (333, 467))
    tela.blit(img_peao[2], (260, 540))
    tela.blit(img_peao[2], (400, 540))
    tela.blit(img_peao[2], (333, 617))

    #Peões amarelos
    tela.blit(img_peao[3], (725, 465))
    tela.blit(img_peao[3], (655, 535))
    tela.blit(img_peao[3], (805, 535))
    tela.blit(img_peao[3], (725, 605))
    return

def Desenha_tabuleiro(img_tab):
    """Implementa a funcionalidade necessária para desenhar o tabuleiro"""
    tela.blit(img_tab, (210, 30))
    return

def Desenha_dado():
    """Implementa a funcionalidade necessária para desenhar o dado."""
   
    return valor_dado



vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (0, 255, 255)

cor_fundo = (139,69,19)

path = '../Assets/'
imagens = []
imagens = Desenha_jogo()

tela = pygame.display.set_mode((1080, 720))
icone = pygame.image.load(path + 'icone_ludo.png')
pygame.display.set_caption('Ludo')
pygame.display.set_icon(icone)
pygame.init()



#player_1 = player('Vermelho')
#player_2 = player('Verde')
#player_3 = player('Azul')
#player_4 = player('Amarelo')
#tabuleiro = Tabuleiro(player_1, player_2, player_3, player_4)

while True:
    tela.fill(cor_fundo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Desenha_tabuleiro(imagens[0])
    Desenha_peao(imagens[1])
    pygame.display.update()