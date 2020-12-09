import pygame
from pygame.locals import *
import time
from Dados import *
from random import randint


def Inicia_telas():
    """Inicia e renderiza a interface gráfica"""
    pygame.font.init()
    pygame.init()
    return


def Desenha_jogo():
    """Renderiza as imagens recebidas"""
    imagens = []
    tabuleiro = pygame.image.load(path+'Tabuleiro.png')
    peao_vermelho = pygame.image.load(path + 'peão_vermelho.png')
    peao_verde = pygame.image.load(path + 'peão_verde.png')
    peao_azul = pygame.image.load(path + 'peão_azul.png')
    peao_amarelo = pygame.image.load(path + 'peão_amarelo.png')
    dado1 = pygame.image.load(path + 'Dado_branco/dice_1.png')
    dado2 = pygame.image.load(path + 'Dado_branco/dice_2.png')
    dado3 = pygame.image.load(path + 'Dado_branco/dice_3.png')
    dado4 = pygame.image.load(path + 'Dado_branco/dice_4.png')
    dado5 = pygame.image.load(path + 'Dado_branco/dice_5.png')
    dado6 = pygame.image.load(path + 'Dado_branco/dice_6.png')
    imagens = [tabuleiro, [peao_vermelho, peao_verde, peao_azul, peao_amarelo], [dado1, dado2, dado3, dado4, dado5, dado6]]
    return imagens
   
def Aonde_clicou():
    """Identifica em que lugar da tela foi clicado"""
    x = 0
    y = 0
    if pygame.mouse.get_pressed() == (1,0,0):
        x,y = pygame.mouse.get_pos()
       
    return [x,y]

def Renderiza_tela_quantos_jogam():
    """Permite selecionar quantos jogadores irão participar da partida"""
    pygame.draw.rect(tela, (122, 122, 122), (210, 30, 660, 660))
    fonte = pygame.font.SysFont("Aerial", 30)
    texto_menu1 = fonte.render("Aperte 2 para 2 jogadores", 1, (255, 255, 255))
    texto_menu2 = fonte.render("Aperte 3 para 3 jogadores", 1, (255, 255, 255))
    texto_menu3 = fonte.render("Aperte 4 para 4 jogadores", 1, (255, 255, 255))
    tela.blit(texto_menu1, (540, 360))
    tela.blit(texto_menu2, (540, 370))
    tela.blit(texto_menu3, (540, 380))
    if pygame.key.get_pressed()[pygame.K_2] != 0:
        return 2
    elif pygame.key.get_pressed()[pygame.K_3] != 0:
        return 3
    elif pygame.key.get_pressed()[pygame.K_4] != 0:
        return 4

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

def Desenha_dado(img_dado):
    """Implementa a funcionalidade necessária para desenhar o dado."""
    tela.blit(img_dado[valor_dado - 1], (50, 50))
    return

def Tela_final():
    for i in range(len(imagens)):
        for j in range(len(imagens[i])):
            pygame.Rect.move(imagens[i][j], (1000, 1000))
   
    if pygame.key.get_pressed()[pygame.K_s] != 0:
        pygame.quit()
    elif pygame.key.get_pressed()[pygame.K_n] != 0:
        Renderiza_tela_quantos_jogam()
    return



vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (0, 255, 255)

cor_fundo = (139,69,19)

path = '../Assets/'
imagens = []
imagens = Desenha_jogo()
valor_dado = 1
apertou = False

tela = pygame.display.set_mode((1080, 720))
icone = pygame.image.load(path + 'icone_ludo.png')
pygame.display.set_caption('Ludo')
pygame.display.set_icon(icone)
Inicia_telas()

while True:
    tela.fill(cor_fundo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    Renderiza_tela_quantos_jogam()
    if Renderiza_tela_quantos_jogam() != 0:
        apertou = True

    if apertou == True:
        Desenha_tabuleiro(imagens[0])
        Desenha_peao(imagens[1])
        Desenha_dado(imagens[2])


        if (Aonde_clicou()[0] > 50 and Aonde_clicou()[1] < 118) and (Aonde_clicou()[1] > 50 and Aonde_clicou()[1] < 118):
            valor_dado = Dados.Clica_dado()

    '''if casa_final['peoes'] == 4:
        apertou = False
        Tela_final()'''

    pygame.display.update()

