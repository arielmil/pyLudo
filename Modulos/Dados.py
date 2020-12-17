import random

def Cria_dado(cor):
    """Cria_dado: Recebe a cor de um jogador, pois a mesma está relacionada com a cor do dado. Cria e retorna um dicionário com a cor do dado e uma lista de sprites, cada elemento dessa lista é o número do dado."""
    
    esse_dado = {"cor": cor, "sprites": ['../Assets/Dado_'+cor+'/dice_1.png',
                    '../Assets/Dado_'+cor+'/dice_2.png',
                    '../Assets/Dado_'+cor+'/dice_3.png',
                    '../Assets/Dado_'+cor+'/dice_4.png',
                    '../Assets/Dado_'+cor+'/dice_5.png',
                    '../Assets/Dado_'+cor+'/dice_6.png']}
    return esse_dado

def Clica_dado(dado):
    """Implementa a função Randint da biblioteca Random. Retorna um número inteiro pseudo-randomizado de 1 (incluído) a 6 (incluído) (1 <= número_gerado <= 6)."""
    
    return random.randint(1,6)

