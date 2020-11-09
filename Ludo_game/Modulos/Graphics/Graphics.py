import pygame
import time

BLACK = (0, 0, 0)
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
    pygame.display.update()
