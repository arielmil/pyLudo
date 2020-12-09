from Peao import *
from Tabuleiro import *
from Dados import *

MENOR_CASA = 1
TABULEIRO = Cria_tabuleiro(0, 0, 1)
MAIOR_CASA = 57

def Inicia_partida():
    #1: Menu
    #2: Determina a vez de um jogador
    #3: Roda o tabuleiro
    #4: Jogador lança o dado
    #5: Jogador escolhe qual peão moverá a quantidade tirada no dado
    #6: Volta ao passo 2
    
    jogadores_restantes = Inicializa_player()
    while jogadores_restantes > 0:
        Escolhe_cor()
    
    Gerencia_partida()
    Roda_tabuleiro()
    Roda_dado()
    Escolhe_peao()
    return

def Gerencia_partida(turno):
    """Implementa a funcionalidade de troca de turnos."""
    

    while peao
    if turno == 4:
        turno = 1
    else:
        turno += 1
    
    if turno == 1:
        #vez do vermelho
        print("Vez do vermelho")        
    elif turno == 2:
        #vez do verde
        print("Vez do verde")        
    elif turno == 3:
        #vez do azul
        print("Vez do azul")        
    elif turno == 4:
        #vez do amarelo
        print("Vez do amarelo")        
    else:
        print("Erro na função Gerencia_partida: jogador não existe")
        return -1

    return turno

def Roda_tabuleiro(tabuleiro):
    """Rotaciona o tabuleiro em 90 graus recalculando as posições de todos os elementos do tabuleiro, após isso chama a função Tabuleiro_animation() do módulo Tabuleiro."""
    if len(tabuleiro) <= 0:
        return -1
    else:
        for casa in tabuleiro:
            if type(casa) == dict: 
                casa["x"] = ALT_TABULEIRO - casa["y"] - LARG_CASA
                casa["y"] = casa["x"]
                if casa["x"] < 0 or casa["y"] < 0:
                    print("ERRO AO ROTACIONAR TABULEIRO, POSIÇÃO DE CASA NEGATIVO")
                    return -2
            else:
                Roda_tabuleiro(casa)
    return 0

def Checa_torres(peao):
    cor = peao["cor"]
    casa = TABULEIRO[peao["casa"]]
    torres = casa["torres"]
    semi_torres = casa["semi_torres"]

    for semi_torre in semi_torres:
        if semi_torre["cor"] == cor:
            return 1
    
    for torre in torres:
        if torre["cor"] == cor:
            return 2
        
    return 0

def Desfaz_torres(peao, option):
    '''Recebe um peao, e um número inteiro. Na casa atual deste peão: Desfaz (remove) uma semi-torre da cor do peão recebido caso o inteiro recebido seja igual a 1, ou Desfaz (regressa) uma torre a uma semi-torre caso o inteiro recebido seja igual a 2. Retorna o inteiro recebido.'''
    cor = peao["cor"]
    casa = TABULEIRO[peao["casa"]]

    if torre_ou_semi-torre == "s" or torre_ou_semi-torre == "S":
        casa["semi_torre"].remove({"cor": cor})
    
    elif torre_ou_semi-torre == "t" or torre_ou_semi-torre == "T":
        casa["torre"].remove({"cor": cor})
        casa["semi_torres"].append({"cor": cor})

    return option
    
def Cria_torres(peao):
    """Implementa no jogo os objetos torre e semi-torre. Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa com algum outro peão da mesma cor. Caso sim, retira o peão desta casa, e cria o objeto semi-torre. Caso ele esteja em uma casa que já tem uma semi-torre, retira a semi torre, e uma torre é Criada no lugar dela. Caso ele esteja em uma casa sem nenhum outro peão, ou já exista uma torre desta cor nesta casa, não cria nada. Retorna -1 caso já exista uma torre dessa cor nesta casa, -2 se não crie nada, 0 caso crie uma semi-torre, ou 1 caso crie uma torre."""
    cor = peao["cor"]
    casa = TABULEIRO[peao["pos"]]
    peoes = casa["peoes"]
    checa = Checa_torres(peao)

    if checa == 1:
        for peao in peoes:
            if peao["cor"] == cor:
                peoes.remove(peao)
        casa["semi_torres"].append({"cor": cor})
        return 1

    elif checa == 2:
        casa["semi_torres"].remove({"cor": cor})
        casa["torres"].append({"cor": cor})
        return 2
    
    return 0

def Controla_peca(peao, numero_dado):
    '''Recebe um peão, um número inteiro representando o valor do dado que acabou de ser jogado. De inicio guarda a casa em que o peão recebido está em uma váriavel e chama Move_peao passando como parametros os dois valores recebidos. Após isso Chama Checa_torres e atribui o resultado em uma váriavel. Após isso atribui o resultado de uma chamada a Desfaz_torres a uma váriavel passando o peão recebido e o resultado de Checa_torres como parametros. Após isso caso Desfaz_torres retorne 0: Atualiza a casa em que o peão estava anteriormente tirando este peão do array de peões desta casa. Após isso chama Move_peão do módulo Peão passando o peão e o número inteiro recebidos como parametros. Por último: atualiza a casa que este peão está, colocando este peão no array de peões desta casa, e chama Cria_torres passando como argumento esse peão.'''
    casa = TABULEIRO[peao["casa"]]
    checa = Move_peao(peao, numero_dado)

    if checa != 0:
        return -1

    checa = Checa_torres(peao)
    checa = Desfaz_torres(peao, checa)

    if checa == 0:
        casa["peoes"].remove(peao)

    TABULEIRO[peao["pos"]]["peoes"].append(peao)

    Cria_torre(peao)

    return 0
    
    
    
def Captura_peao(peao):
    """É chamada sempre após Move_peão(). Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa com algum outro peão de outra cor, cajo esteja, Manda_para_casa() sera executada como esse outro peão como argumento. Retorna 0 Caso um peão seja capturado, 1 caso contrário, e -1 em caso de erro."""
    if (type(peao) == dict):
        if (("pos") in peao):
            casa_peao = int(peao["pos"]) #Converti para inteiro só para garantir.
            if (casa_peao < MENOR_CASA or casa_peao > MAIOR_CASA):
                print("\nA posição deste peão não é um valor valido.")
                return -3
            if (len (tabuleiro[casa_peao]["peoes"])) > 0 and (len (tabuleiro[casa_peao]["peoes"])) < 3:
                for peca in tabuleiro[casa_peao]["peoes"]:
                    if peca["cor"] != peao["cor"]:
                        Manda_para_casa(peca)
                        return 0
          
            print("Não existem peões para serem capturados nessa casa.")
            return -2
        print("Erro: dicionário recebido não é um peão.")
        return -4
    print("Erro: parametro recebido não é um dicionário.")
    return -1

def Manda_para_casa(peao):
    """É chamada sempre após a função Captura_peao. faz com que o peão capturado retorne para sua posição inicial. Retorna 0 caso rode com sucesso, e -1 caso contrário."""
    if (type(peao) == dict): # and checar se naquele dict tem um campo chamado fin_pos#
        peao["fin_pos"] = 0
        return 0
    return -1

def Inicializa_player():
    """Recebe um número inteiro de 2 a 4 da função Quantos_jogam do módulo Main, e Inicializa e retorna um array de jogadores com o número recebido."""
    return

def Escolhe_peao():
    """Permite que o jogador escolha um peão retornando um número inteiro de 0 (incluso) a 3 (incluso) de forma a qual cada número está associado a um dos 4 peões, caso o jogador clique no peão desejado."""
    return

def Escolhe_cor():
    """Associa uma cor a uma instância de jogador."""
    return 0

