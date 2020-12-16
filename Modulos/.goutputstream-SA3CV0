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
    opcao_2j = pygame.draw.rect(tela, (0, 0, 0), (390, 290, 50, 50))
    opcao_3j = pygame.draw.rect(tela, (0, 0, 0), (390, 390, 50, 50))
    opcao_4j = pygame.draw.rect(tela, (0, 0, 0), (390, 490, 50, 50))
    fonte = pygame.font.SysFont("Arial", 30)
    texto_menu = fonte.render("Quantidade de jogadores:", 1, (255, 255, 25))
    texto_menu_2j = fonte.render("2", 1, (255, 255, 255))
    texto_menu_3j = fonte.render("3", 1, (255, 255, 255))
    texto_menu_4j = fonte.render("4", 1, (255, 255, 255))
    tela.blit(texto_menu, (400, 100))
    tela.blit(texto_menu_2j, (400, 300))
    tela.blit(texto_menu_3j, (400, 400))
    tela.blit(texto_menu_4j, (400, 500))
    if (Aonde_clicou()[0] > 390 and Aonde_clicou()[0] < 440) and (Aonde_clicou()[1] > 290 and Aonde_clicou()[1] < 340):
        return 2
    elif (Aonde_clicou()[0] > 390 and Aonde_clicou()[0] < 440) and (Aonde_clicou()[1] > 390 and Aonde_clicou()[1] < 440):
        return 3
    elif (Aonde_clicou()[0] > 390 and Aonde_clicou()[0] < 440) and (Aonde_clicou()[1] > 490 and Aonde_clicou()[1] < 540):
        return 4

    return 0

def Desenha_peao(img_peao):
    """Implementa a funcionalidade necessária para desenhar os peões"""
    #Peões vermelhos
    verm1 = tela.blit(img_peao[0], (285, 85))
    verm2 = tela.blit(img_peao[0], (205, 155))
    verm3 = tela.blit(img_peao[0], (355, 155))
    verm4 = tela.blit(img_peao[0], (285, 225))

    #Peões verdes
    verd1 = tela.blit(img_peao[1], (725, 30))
    verd2 = tela.blit(img_peao[1], (655, 110))
    verd3 = tela.blit(img_peao[1], (795, 110))
    verd4 = tela.blit(img_peao[1], (725, 180))

    #Peões azuis
    azul1 = tela.blit(img_peao[2], (333, 522))
    azul2 = tela.blit(img_peao[2], (260, 595))
    azul3 = tela.blit(img_peao[2], (400, 595))
    azul4 = tela.blit(img_peao[2], (333, 672))

    #Peões amarelos
    amar1 = tela.blit(img_peao[3], (770, 478))
    amar2 = tela.blit(img_peao[3], (700, 548))
    amar3 = tela.blit(img_peao[3], (850, 548))
    amar4 = tela.blit(img_peao[3], (770, 618))

    #Diferença: 44 pixels
    tela.blit(img_peao[2], (482, 618))

    lista_peoes = [verm1, verm2, verm3, verm4, verd1, verd2, verd3, verd4, azul1, azul2, azul3, azul4, amar1, amar2, amar3, amar4]
    return lista_peoes

def Desenha_tabuleiro(img_tab):
    """Implementa a funcionalidade necessária para desenhar o tabuleiro"""
    tela.blit(img_tab, (165, 0))
    return

def Desenha_dado(img_dado):
    """Implementa a funcionalidade necessária para desenhar o dado."""
    if dado_usado["num"] == None:
        tela.blit(img_dado[0], (50, 50))
    else:
        tela.blit(img_dado[dado_usado["num"] - 1], (50, 50))
    return

def Move_peao(valor_dado, peao):
    #while valor_dado > 0:
        #peao = ((coordenadas[casa][0] + coordenadas[casa][2])/2, (coordenadas[casa][1] + coordenadas[casa][3])/2)
    return


def Posicao_peoes():
    """Retorna o número da casa em que os peões estão."""
    for peao in range(len(coordenadas)):
        if (Aonde_clicou()[0] > coordenadas[peao][0] and Aonde_clicou()[0] < coordenadas[peao][2]) and (Aonde_clicou()[1] > coordenadas[peao][1] and Aonde_clicou()[1] < coordenadas[peao][3]) :
            return peao
    return 0

def Clica_casa():
    """Retorna o valor absoluto da casa"""
    click = pygame.font.SysFont("Arial", 15)
    for casa in range(len(coordenadas)):
        if (Aonde_clicou()[0] > coordenadas[casa][0] and Aonde_clicou()[0] < coordenadas[casa][2]) and (Aonde_clicou()[1] > coordenadas[casa][1] and Aonde_clicou()[1] < coordenadas[casa][3]) :
            return casa
    return 0

def Localiza_casas():
    coordenadas = []
    num = pygame.font.SysFont("Arial", 15)
    for casa in range(58):
        #Casa inicial
        if casa == 0:
            coordenadas.append([0, 0, 0, 0])

        #Primeira casa depois de sair da casa inicial
        elif casa == 1:
            coordenadas.append([517, 658, 473, 616])

        #Norte
        elif (casa > 1 and casa < 6) or (casa > 11 and casa < 14) or (casa > 19 and casa < 25) or (casa > 51):
            coordenadas.append([coordenadas[casa-1][0], coordenadas[casa-1][1] - 44, coordenadas[casa-1][2], coordenadas[casa-1][3] - 44])

        #Noroeste
        elif casa == 6:
            coordenadas.append([coordenadas[casa-1][0] - 45, coordenadas[casa-1][1] - 45, coordenadas[casa-1][2] - 45, coordenadas[casa-1][3] - 45])

        #Oeste
        elif (casa > 6 and casa < 12) or (casa > 39 and casa < 45) or (casa == 51):
            coordenadas.append([coordenadas[casa-1][0] - 44, coordenadas[casa-1][1], coordenadas[casa-1][2] - 44, coordenadas[casa-1][3]])
        
        #Nordeste
        elif casa == 19:
            coordenadas.append([coordenadas[casa-1][0] + 45, coordenadas[casa-1][1] - 45, coordenadas[casa-1][2] + 45, coordenadas[casa-1][3] - 45])

        #Leste
        elif (casa >= 14 and casa < 19) or (casa >= 25 and casa < 27) or (casa > 32 and casa <= 37):
            coordenadas.append([coordenadas[casa-1][0] + 44, coordenadas[casa-1][1], coordenadas[casa-1][2] + 44, coordenadas[casa-1][3]])

        #Sudeste
        elif casa == 32:
            coordenadas.append([coordenadas[casa-1][0] + 45, coordenadas[casa-1][1] + 45, coordenadas[casa-1][2] + 45, coordenadas[casa-1][3] + 45])

        #Sul
        elif (casa > 26 and casa < 32) or (casa > 37 and casa < 40) or (casa > 45 and casa < 52):
            coordenadas.append([coordenadas[casa-1][0], coordenadas[casa-1][1] + 44, coordenadas[casa-1][2], coordenadas[casa-1][3] + 44])

        #Sudoeste
        elif casa == 45:
            coordenadas.append([coordenadas[casa-1][0] - 45, coordenadas[casa-1][1] + 45, coordenadas[casa-1][2] - 45, coordenadas[casa-1][3] + 45])


        texto = num.render(str(casa), 1, (0, 0, 0))
        casa_centro = ((coordenadas[casa][0] + coordenadas[casa][2])/2, (coordenadas[casa][1] + coordenadas[casa][3])/2)
        tela.blit(texto, tuple(casa_centro))

    return coordenadas

def Tela_final():
    if pygame.key.get_pressed()[pygame.K_s] != 0:
        return True
    elif pygame.key.get_pressed()[pygame.K_n] != 0:
        return False
    return 0



vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (0, 255, 255)

cor_fundo = (139,69,19)

path = '../Assets/'
imagens = []
imagens = Desenha_jogo()
jogo = False
final = False
dado_usado = Cria_dado("branco")

tela = pygame.display.set_mode((1080, 748))
icone = pygame.image.load(path + 'icone_ludo.png')
pygame.display.set_caption('Ludo')
pygame.display.set_icon(icone)
Inicia_telas()

while True:
    tela.fill(cor_fundo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Menu inicial
    if jogo == False and final == False:
        Renderiza_tela_quantos_jogam()
        if Renderiza_tela_quantos_jogam() != 0:
            jogo = True

    #Durante o jogo
    elif jogo == True:
        Desenha_tabuleiro(imagens[0])
        Desenha_peao(imagens[1])
        Desenha_dado(imagens[2])
        coordenadas = Localiza_casas()
        if Clica_casa() != 0:
            print(Clica_casa())

        if (Aonde_clicou()[0] > 50 and Aonde_clicou()[1] < 118) and (Aonde_clicou()[1] > 50 and Aonde_clicou()[1] < 118):
            Clica_dado(dado_usado)

    #Fim de jogo
    elif final == True:
        jogo = False
        Tela_final()
        if Tela_final() == True:
            final = False
        elif Tela_final == False:
            pygame.quit()

    pygame.display.update()

