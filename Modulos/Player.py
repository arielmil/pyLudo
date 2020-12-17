def Cria_jogador(debug):
    """Usado para criar um jogador"""

    limit = 30
    escolhendo = True
    controle_debug_tentativas = 0

    while (escolhendo):

        if debug:
            
            if debug == 1:
                nome = "Teste"                

            elif debug == 2:
                nome = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
        else:
            nome = str(input("\nPor favor, digite o seu nome de jogo ou aperte enter, sair, Sair ou SAIR para não escolher: "))

        if len(nome) > limit:
            print("\nErro: o nome deve ter no máximo 30 caracteres.")

            if debug:
                return -1

        elif nome == "sair" or nome == "Sair" or nome == "SAIR" or nome == "":
            return -1

        else:
            escolhendo = False

        jogador = {"nome": nome}
        return jogador
