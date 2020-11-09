def Cria_usuario():
    """Usado para criar um usuário"""
    LIMITE = 30
    escolhendo = True
    i = 0
    while (escolhendo == True and i < 10):
        nome = str(input("\nPor favor, escolha seu nome de usuário, ou aperte enter para não escolher: "))
        if len(nome) > LIMITE:
            print("\nErro: o nome deve ter no máximo 30 caracteres.")
            i = i + 1
        elif nome == "":
            return -1
        else:
            escolhendo = False
    if (i == 10):
    	print("Usuário ultrapassou o limite de tentativas para criação de nome. Por favor, tente novamente.")
    	return -2

    i = 0
    escolhendo = True
    while (escolhendo == True and i < 10):
        senha = str(input("\nPor favor, digite a senha a ser cadastrada: "))
        if len(senha) > LIMITE:
            print("\nErro: a senha deve ter no máximo 30 caracteres.")
            i = i + 1
        elif senha == "":
            return -3
        else:
            escolhendo = False
    if (i == 10):
    	print("Usuário ultrapassou o limite de tentativas para criação de senha. Por favor, tente novamente.")
    	return -4
    usuario = {"nome": nome, "senha": senha}
    return usuario
