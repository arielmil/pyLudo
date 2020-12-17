def Cria_peao(cor, pos):
    """Cria_peao: Recebe uma cor (string), e retorna um dicionario peão com as informações úteis para o jogo (cor, posicao, e sprite)."""

    esse_peao = {"cor":cor, "pos": pos, "sprite": '../Assets/peão'+'_' + cor +'.png'}
    return esse_peao

def Cria_peoes(cor):
    """Recebe uma string representando uma cor válida. Utilizando a função Cria_peao, cria um array de 4 peões com a cor selecionada, e com suas respectivas posições em suas respectivas casas iniciais. Retorna este array."""
    
    peoes = []
    #Tratar aqui as quatro posicoes iniciais para as 4 cores diferentes.
    for i in range(0,4):
        peoes.append(Cria_peao(cor,0))
    return peoes

def Move(peao,numero_dado):
    """Recebe um valor da função "Joga_dado" do módulo Dado, e atualiza o campo "casa" do peão recebido com o valor. Retorna -1 caso receba um valor incorreto, 1 caso o peão passado por parametro já esteja em sua última posição (final do tabuleiro), ou 0 caso a casa_relativa em que ele está seja atualizada."""
    
    if (numero_dado <= 0 or numero_dado > 6):
        print("\nNumero de dado recebido invalido.")
        return -1
    if (numero_dado + peao["pos"]) <= 57:
        peao["pos"] = numero_dado + peao["pos"]
        return 0
    else:
        #Peao nao pode se mover.
        return 1
        
__all__ = ['Cria_peoes', 'Move']
