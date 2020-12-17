def Cria_jogador(debug_helper):
    """Para ser usado em conjunto com o banco de dados: Entra em um loop até que seja digitada uma sequência de caracteres que será o nome do jogador, ou até que o jogador resolva sair. Retorna um dicionario chamado jogador com um campo nome, ou -1 caso seja digitado: sair, Sair, SAIR, ou nada. Pode receber opcionalmente um inteiro chamado debug que é usado nos testes unitários."""

    limit = 30
    escolhendo = True
    controle_debug_tentativas = 0

    while (escolhendo):

        if debug_helper:
            
            if debug_helper == 1:
                nome = "Teste"                

            elif debug_helper == 2:
                nome = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
        else:
            nome = str(input("\nPor favor, digite o seu nome de jogo ou aperte enter, sair, Sair ou SAIR para não escolher: "))

        if len(nome) > limit:
            print("\nErro: o nome deve ter no máximo 30 caracteres.")

            if debug_helper:
                return -1

        elif nome == "sair" or nome == "Sair" or nome == "SAIR" or nome == "":
            return -1

        else:
            escolhendo = False

        jogador = {"nome": nome}
        return jogador
