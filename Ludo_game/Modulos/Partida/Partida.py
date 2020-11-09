from ..Tabuleiro import *

tabuleiro = Cria_tabuleiro()

def Gerencia_partida():
    """Implementa a funcionalidade de troca de turnos."""
    return

def Roda_tabuleiro():
    """Rotaciona o tabuleiro em 90 graus re calculando as posições de todos os elementos do tabuleiro, após isso chama a função Tabuleiro_animation() do módulo Tabuleiro."""
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
                Roda_Tabuleiro(casa)
    return 0

def Cria_torre():
    """Implementa no jogo os objetos Torre e Semi-Torre. É chamada sempre após Move_peão(). Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa com algum outro peão da mesma cor. Caso sim, cria o objeto Semi-Torre. Caso ele esteja em uma casa que já tem uma Semi-Torre, uma Torre é Criada no lugar dela. Caso ele esteja em uma casa sem nenhum outro peão, retorna 0."""
    return

def Captura_peao(peao):
    """É chamada sempre após Move_peão(). Recebe como argumento o peão que acabou de ser movido, e verifica através dele se ele está em uma casa com algum outro peão de outra cor, cajo esteja, Manda_para_casa() sera executada como esse outro peão como argumento. Retorna 0 Caso um peão seja capturado, 1 caso contrário, e -1 em caso de erro."""
    if (type(peao) == dict): # and checar se naquele dict tem um campo chamado fin_pos#
        casa_peao = peao["fin_pos"]
        if (len (tabuleiro[casa_peao])["peoes"]) > 0 and (len (tabuleiro[casa_peao])["peoes"]) < 2:
            for peca in tabuleiro[casa_peao]["peoes"]:
                if peca["cor"] != peao["cor"]:
                    Manda_para_casa(peca)
                    return 0
        print("Não existem peões para serem capturados nessa casa.")
        return 1
    print("Erro: parametro recebido não é um peão")
    return -1

def Desmancha_torre(peao):
    return 0

def Manda_para_casa(peao):
    """É chamada sempre após a função Captura_peao. faz com que o peão capturado retorne para sua posição inicial. Retorna 0 caso rode com sucesso, e -1 caso contrário."""
    if (type(peao) == dict): # and checar se naquele dict tem um campo chamado fin_pos#
        peao["fin_pos"] = 0
        return 0
    return -1

def Inicializa_player():
    """Recebe um número inteiro de 2 a 4 da função Quantos_jogam do módulo Main, e Inicializa e retorna um array de jogadores com o número recebido."""
    return

def Roda_dado():
    """Faz um jogador jogue o Dado. Para isso, utiliza a função Joga_dado() do módulo Dado, caso o jogador clique no icone do Dado."""
    return

def Escolhe_peao():
    """Permite que o jogador escolha um peão retornando um número inteiro de 0 (incluso) a 3 (incluso) de forma a qual cada número está associado a um dos 4 peões, caso o jogador clique no peão desejado."""
    return
