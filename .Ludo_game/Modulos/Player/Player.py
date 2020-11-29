def Cria_jogador():
    limit = 30
    escolhendo = True
    while (escolhendo):
        nome = str(input("\nPor favor, digite o seu nome de jogo ou aperte enter para não escolher:\n"))
        if len(nome) > limit:
            print("\nErro: o nome deve ter no máximo 30 caracteres.")
        elif nome == "":
            return -1
        else:
            escolhendo = False
    jogador = {"nome": nome}
    return jogador