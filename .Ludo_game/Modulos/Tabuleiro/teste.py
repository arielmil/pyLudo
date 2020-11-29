from Tabuleiro import *

pos_ini = {"x":0,"y":0}
teste = Cria_tabuleiro(pos_ini,2,True)

for i in range(len(teste)):
    if (teste[i] == []):
        print(teste)
        print(i)
print("\n\n")


'''def Printa_tabuleiro(tabuleiro):
    """Usada para debugging"""
    i = 1
    while (i < 58):
        print("Posição x da casa: "+  str(i) +": " + str(tabuleiro[i]["x"])+" Posição y da casa "+str(i) + ": " + str(tabuleiro[i]["y"]))
        i = i + 1
    return 0

Printa_tabuleiro(teste)'''
