import random

def Cria_dado(cor):
    """Cria um dado"""
    esse_dado = {"cor": cor, "sprites": ['../Assets/Dado_'+cor+'/dice_1.png',
                    '../Assets/Dado_'+cor+'/dice_2.png',
                    '../Assets/Dado_'+cor+'/dice_3.png',
                    '../Assets/Dado_'+cor+'/dice_4.png',
                    '../Assets/Dado_'+cor+'/dice_5.png',
                    '../Assets/Dado_'+cor+'/dice_6.png']}
    return esse_dado

def Clica_dado(dado):
    """Gera um número randomico entre [1,6]"""
    return random.randint(1,6)



