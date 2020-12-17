from Peao import *
from Tabuleiro import *
from Banco_de_dados import *
from Dados import *

MENOR_CASA = 1
TABULEIRO = Cria_tabuleiro({"x": 658, "y": 616}, 44)
MAIOR_CASA = 57

#OBS: Foi obtida permissão do professor para fazer com que a casa guarde quantos peoes tem nela.

def Gerencia_rodada(peao, casa_clicada, dado):
    """Implementa uma rodada do jogo."""

    flag = 0
    numero_dado = 6

    while (True):

        if numero_dado != 6:
            break

        num_dado = Clica_dado(dado)
        checa = Controla_peca(peao, numero_dado)

        while (checa == 1):
            numero_dado = Clica_dado(dado)
            checa = Controla_peca(peao, numero_dado)

        if flag == 1:
            break

        if num_dado == 6:
            flag = 1

    return 0

def Checa_torres(peao):
    """Recebe um peão, e checa se na sua posição relativa existe uma semi_torre, ou torre de sua cor. Retorna 1 caso exista uma semi_torre, 2 caso exista uma torre, 0 caso caso não existam nenhuma das duas."""

    cor = peao["cor"]
    numero_casa = Converte_posicao(cor, peao["pos"])
    casa_relativa = TABULEIRO[numero_casa]
    torres = casa_relativa["torres"]
    semi_torres = casa_relativa["semi_torres"]

    for semi_torre in semi_torres:
        if semi_torre["cor"] == cor:
            return 1
    
    for torre in torres:
        if torre["cor"] == cor:
            return 2
        
    return 0

def Desfaz_torres(peao, option):
    """Recebe um peao, e um número inteiro. Na casa_relativa atual deste peão: Desfaz (remove) uma semi-torre da cor do peão recebido caso o inteiro recebido seja igual a 1, ou Desfaz (regressa) uma torre a uma semi-torre caso o inteiro recebido seja igual a 2. Retorna o inteiro recebido."""

    cor = peao["cor"]
    numero_casa = Converte_posicao(cor, peao["pos"])
    casa_relativa = TABULEIRO[numero_casa]

    if option == 1:
        casa_relativa["semi_torre"].remove({"cor": cor})
        casa_relativa["peoes"].append(peao)
    
    elif option == 2:
        casa_relativa["torre"].remove({"cor": cor})
        casa_relativa["semi_torres"].append({"cor": cor})

    return option
    
def Cria_torres(peao):
    """Implementa no jogo os objetos torre e semi-torre. É chamada sempre após Controla_peca. Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa_relativa com algum outro peão da mesma cor. Caso sim, retira o peão desta casa, e cria o objeto semi-torre. Caso ele esteja em uma casa_relativa que já tem uma semi-torre, retira a semi torre, e uma torre é Criada no lugar dela. Caso ele esteja em uma casa_relativa sem nenhum outro peão, ou já exista uma torre desta cor nesta casa, não cria nada. Retorna -1 caso já exista uma torre dessa cor nesta casa, -2 se não crie nada, 0 caso crie uma semi-torre, ou 1 caso crie uma torre. """
    
    cor = peao["cor"]
    numero_casa = Converte_posicao(cor, peao["pos"])
    casa_relativa = TABULEIRO[numero_casa]
    peoes = casa_relativa["peoes"]
    checa = Checa_torres(peao)

    if checa == 0:
        for peao in peoes:
            if peao["cor"] == cor:
                peoes.remove(peao)
        casa_relativa["semi_torres"].append({"cor": cor})
        return 1

    elif checa == 1:
        casa_relativa["semi_torres"].remove({"cor": cor})
        casa_relativa["torres"].append({"cor": cor})
        return 2
    
    return 0

def Controla_peca(peao, numero_dado):
    """Recebe um peão, um número inteiro representando o valor do dado que acabou de ser jogado. De inicio guarda a casa_relativa em que o peão recebido está em uma váriavel e chama Move_peao passando o peão e o número inteiro recebidos como parametros também guardando seu retorno em uma variável passando como parametros os dois valores recebidos. Após isso, caso Move_peão tenha retornado 0: Chama Checa_torres e atribui o resultado em uma váriavel. Após isso atribui o resultado de uma chamada a Desfaz_torres a uma váriavel passando o peão recebido e o resultado de Checa_torres como parametros. Após isso caso Desfaz_torres retorne 0 ou 1: Atualiza a casa_relativa em que o peão estava anteriormente tirando este peão do array de peões desta casa. Por último: atualiza a casa_relativa que este peão está, colocando este peão no array de peões desta casa, e chama Cria_torres passando como argumento esse peão. Retorna -1 caso o peão recebido não possa se movimentar, ou 0 caso o contrário."""
    
    cor = peao["cor"]
    numero_casa = Converte_posicao(cor, peao["pos"])
    casa_relativa = TABULEIRO[numero_casa]
    
    checa = Checa_torres(peao)
    checa = Desfaz_torres(peao, checa)

    if checa == 0 or checa == 1:
        casa_relativa["peoes"].remove(peao)

    checa = Move_peao(peao, numero_dado)

    if checa != 0:
        return -1

    numero_casa = Converte_posicao(cor, peao["pos"])
    casa_relativa = TABULEIRO[numero_casa]
    
    casa_relativa["peoes"].append(peao)
    
    checa = Captura_peao(peao)

    Cria_torre(peao)
    
    #Joga de novo
    if checa == 0:
        return 1
        
    return 0
    
def Captura_peao(peao):
    """É chamada sempre após a função Controla_peca. Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa_relativa com algum outro peão de outra cor, cajo esteja, Manda_para_casa sera executada como esse outro peão como argumento. Retorna 0 Caso um peão seja capturado, 1 caso contrário, e -1 em caso de erro."""

    if (type(peao) == dict):
        
        if (("pos") in peao):
            cor = peao["cor"]
            numero_casa = Converte_posicao(cor, peao["pos"])
            
            if numero_casa < MENOR_CASA or numero_casa > MAIOR_CASA:
                print("\nA posição deste peão não é um valor valido.")
                return -1

            casa_relativa = TABULEIRO[numero_casa]
            peoes = casa_relativa["peoes"]
            
            for peao in peoes:
                
                if peao["cor"] != cor:
                    Manda_para_casa(peao)
                    return 1
          
            print("Não existem peões para serem capturados nessa casa.")
            return 0
        
        print("Erro: dicionário recebido não é um peão.")
        return -2
    
    print("Erro: parametro recebido não é um dicionário.")
    return -3

def Manda_para_casa(peao):
    """É chamada sempre após a função Captura_peão. faz com que o peão capturado retorne para sua posição inicial. Retorna 0 case rode com sucerro, e -1 caso contrário."""

    if (type(peao) == dict):
        if "pos" in peao:
            peao["pos"] = 0
        return 0
    
    return -1

def Checa_disponibilidade_peao(cor, numero_dado, casa):
    """Recebe um peao, e dois inteiros representando o número de dado que acabou de ser tirado, e uma posição (número de casa). E utilizando a função Checa_disponibilidade do módulo Tabuleiro checa se o peão recebido pode se movimentar baseado no número de dado tirado. Retorna -2 caso não existam peões na posição recebida, -1 caso exista, mas esse peão não pode se mover, ou a casa que ele está caso exista, e possa."""

    numero_casa = Converte_posicao(cor, casa)
    casa_relativa = TABULEIRO[numero_casa]

    #aqui tratar caso casa_relativa seja igual a 0

    peoes = casa_relativa["peoes"]

    checa = None

    for peao in peoes:
        if peao["cor"] == cor:

            if casa == 0:
                if numero_dado != 6:
        
                    #Peao esta na posicao recebida, porem nao pode andar.
                    return -1
            
                #Peao esta na posicao recebida, e pode andar.
                return 1
        
            checa = Checa_disponibilidade(casa + numero_dado, cor)

            if checa == -1:

                #Peao esta na posicao recebida, porem nao pode andar.
                return -1

            #Peao esta na posicao recebida, e pode andar.
            return 1

    #Peao nao esta na posicao recebida.
    return -2

    
def Checa_peao(jogador, casa_clicada, numero_dado):
    """Recebe um jogador provido pela funcao Quantos_jogam do modulo Main, dois números inteiros representando uma posicao (numero de casa), e o numero do dado que acabou de ser tirado. Permite que o jogador escolha um peão para se mover. Retorna o índice desse peão no array de peões dentro do jogador, -2 caso nenhum peão válido esteja na casa clicada, ou -1 caso esteja porém não pode se mover."""

    peoes = jogador[1]

    cor = peoes[0]["cor"]
    
    checa = Checa_disponibilidade_peao(cor, numero_dado, casa_clicada)

    if checa < 1:
        #Esse peao nao pode andar
        return checa

    for num in range(0, len(peoes)):
        if peoes[num]["pos"] == casa_clicada:
            return num
            
    return -2
    
__all__ = ['Gerencia_rodada', 'Checa_peao']
