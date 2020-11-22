import pygame
from pygame.locals import *
import time
from Partida import *

def Inicia_telas():
    """Inicia e renderiza a interface gráfica"""
    pygame.init()
    tela = pygame.display.set_mode((1020, 894))
    pygame.display.set_caption("Ludo")
    cor_fundo = (122, 122, 122)
    valor_dado = 1
    imagens = Desenha_jogo()
    xi1 = 265
    xi2 = 315
    xi3 = 800
    xi4 = 850
    yi1 = 125
    yi2 = 175
    yi3 = 675
    yi4 = 725
    vez = 0 #0 = vermelho, 1 = verde, 2 = azul, 3 = amarelo
    
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        
        tela.fill(cor_fundo)
        Desenha_tabuleiro(tela, imagens[0][0])
        
        #Posições iniciais dos peões
        #Peões vermelhos
        tela.blit(imagens[1][valor_dado - 1], (29, 800))
        tela.blit(imagens[2][0][0], (xi1, yi1))
        tela.blit(imagens[2][0][1], (xi2, yi2))
        tela.blit(imagens[2][0][2], (xi2, yi1))
        tela.blit(imagens[2][0][3], (xi1, yi2))
        #Peões verdes
        tela.blit(imagens[2][1][0], (xi3, yi1))
        tela.blit(imagens[2][1][1], (xi4, yi2))
        tela.blit(imagens[2][1][2], (xi4, yi1))
        tela.blit(imagens[2][1][3], (xi3, yi2))
        #Peões azuis
        tela.blit(imagens[2][2][0], (xi1, yi3))
        tela.blit(imagens[2][2][1], (xi2, yi4))
        tela.blit(imagens[2][2][2], (xi2, yi3))
        tela.blit(imagens[2][2][3], (xi1, yi4))
        #Peões amarelos
        tela.blit(imagens[2][3][0], (xi3, yi3))
        tela.blit(imagens[2][3][1], (xi4, yi4))
        tela.blit(imagens[2][3][2], (xi4, yi3))
        tela.blit(imagens[2][3][3], (xi3, yi4))
        
        Desenha_peao(tela, imagens, valor_dado, xi1, xi2, xi3, xi4, yi1, yi2, yi3, yi4, vez)
        
        if Aonde_clicou() != 0:
            if (Aonde_clicou()[0] > 29 and Aonde_clicou()[0] < 97) and (Aonde_clicou()[1] > 800 and Aonde_clicou()[1] < 868):
                valor_dado = Clica_dado(dado)
                time.sleep(0.01)
                

        pygame.display.update()


def Desenha_jogo():
    """Renderiza as imagens recebidas"""
    imgs_tabuleiro = []
    imgs_dado = []
    peoes_vermelhos = []
    peoes_verdes = []
    peoes_azuis = []
    peoes_amarelos = []
    imgs_peao = []
    imagens = []
    '''
    img_tabuleiro = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Board.jpg')
    img_dado1 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_1.png')
    img_dado2 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_2.png')
    img_dado3 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_2.png')
    img_dado4 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_2.png')
    img_dado5 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_5.png')
    img_dado6 = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/Dado_branco/dice_6.png')
    img_peao_vermelho = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/peão_vermelho.png')
    img_peao_verde = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/peão_verde.png')
    img_peao_azul = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/peão_azul.png')
    img_peao_amarelo = pygame.image.load('C:/Users/guilh/Documents/Matéria/8º Período/Programção Modular/pyLudo/Assets/peão_amarelo.png')
    '''
    #Única imagem de tabuleiro
    imgs_tabuleiro.append(img_tabuleiro) 
    
    #Valores do dado
    imgs_dado.append(img_dado1)
    imgs_dado.append(img_dado2)
    imgs_dado.append(img_dado3)
    imgs_dado.append(img_dado4)
    imgs_dado.append(img_dado5)
    imgs_dado.append(img_dado6)
    
    #Todos os peões
    for i in range(4):
        peoes_vermelhos.append(img_peao_vermelho)
        peoes_verdes.append(img_peao_verde)
        peoes_azuis.append(img_peao_azul)
        peoes_amarelos.append(img_peao_amarelo)        
    imgs_peao = [peoes_vermelhos, peoes_verdes, peoes_azuis, peoes_amarelos]
    
    imagens = [imgs_tabuleiro, imgs_dado, imgs_peao]
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

def Desenha_peao(tela, imagens, valor_dado, xi1, xi2, xi3, xi4, yi1, yi2, yi3, yi4, vez):
    """Desenha a movimentação do peão"""
    #for i in range(valor_dado):
        #if(vez == 0):
            #if Aonde_clicou() >= 
    return

def Desenha_tabuleiro(tela, imagem):
    """Implementa a funcionalidade necessária para desenhar o tabuleiro"""
    return tela.blit(imagem, (126,0))

def Desenha_dado():
    """Implementa a funcionalidade necessária para desenhar o dado."""
    
    return valor_dado


Inicia_telas()
