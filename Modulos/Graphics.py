import pygame
from pygame.locals import *
import time
from Dados import *


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
    dado1 = pygame.image.load(path + 'Dado_branco/dice1.png')
    dado2 = pygame.image.load(path + 'Dado_branco/dice2.png')
    dado3 = pygame.image.load(path + 'Dado_branco/dice3.png')
    dado4 = pygame.image.load(path + 'Dado_branco/dice4.png')
    dado5 = pygame.image.load(path + 'Dado_branco/dice5.png')
    dado6 = pygame.image.load(path + 'Dado_branco/dice6.png')
    imagens = [tabuleiro, [peao_vermelho, peao_verde, peao_azul, peao_amarelo], [dado1, dado2, dado3, dado4, dado5, dado6]]
    return imagens
   
def Aonde_clicou():
    """Identifica em que lugar da tela foi clicado"""
    onde = 0
    if pygame.mouse.get_pressed() == (1,0,0):
        onde = pygame.mouse.get_pos()
       
    return onde

def Renderiza_tela_quantos_jogam():
    """Permite selecionar quantos jogadores irão participar da partida"""
    fundo_menu = tela.draw.rect(tela, (0, 0, 0), [210, 30, 870, 690])
    opcao_2j = tela.draw.circle(tela, (255, 255, 255), [570, 390], 10)
    opcao_3j = tela.draw.circle(tela, (255, 255, 255), [630, 450], 10)
    opcao_4j = tela.draw.circle(tela, (255, 255, 255), [690, 510], 10)
    
    if Aonde_clicou() in opcao_2j:
        quant_jogadores = 2
    elif Aonde_clicou() in opcao_3j:
        quant_jogadores = 3
    elif Aonde_clicou() in opcao_4j:
        quant_jogadores = 4
        
    return quant_jogadores

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
    valor_dado = 1
    tela.blit(img_dado[valor_dado - 1], (50, 50))
    return
    
def Tela_final():
    fundo_final = tela.draw.rect(tela, (0, 0, 0), [210, 30, 870, 690])
    botao_sair = tela.draw.rect(tela, (122, 122, 122), [210, 640, 310, 690])
    botao_reiniciar = tela.draw.rect(tela, (122, 122, 122), [770, 640, 870, 690])
    
    if Aonde_clicou() in botao_sair:
        #sai do jogo
    elif Aonde_clicou() in botao_reiniciar:
        #inicia uma nova partida
    return



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
    Renderiza_tela_quantos_jogam()
    Desenha_tabuleiro(imagens[0])
    Desenha_peao(imagens[1])
    Desenha_dado(imagens[2])
    pygame.display.update()