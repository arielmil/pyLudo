import random
import pygame
import time

def Cria_dado(cor):
    """Cria um dado"""
    esse_dado = {"num": None, "sprites": ['../../Assets/Dado_'+cor+'/dice_1.png',
                    '../../Assets/Dado_'+cor+'/dice_2.png',
                    '../../Assets/Dado_'+cor+'/dice_3.png',
                    '../../Assets/Dado_'+cor+'/dice_4.png',
                    '../../Assets/Dado_'+cor+'/dice_5.png',
                    '../../Assets/Dado_'+cor+'/dice_6.png']}
    return esse_dado

def Clica_dado(dado):
    """Gera um número randomico entre [1,6]"""
    dado["num"] = random.randint(1,6)
    return 0


