def Cria_jogador():
    """Usado para criar um jogador"""
    limit = 30
    escolhendo = True
    while (escolhendo):
        nome = str(input("\nPor favor, digite o seu nome de jogo ou aperte enter, sair, Sair ou SAIR para não escolher: "))
        if len(nome) > limit:
            print("\nErro: o nome deve ter no máximo 30 caracteres.")
        elif nome == "sair" or nome == "Sair" or nome == "SAIR" or nome == "":
            return -1
        else:
            escolhendo = False
    jogador = {"nome": nome}
    return jogador
