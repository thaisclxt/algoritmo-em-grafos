from itertools import permutations

def ordenacao_topologica(grafo):
    visitados = set()
    pilha = []

    def busca_em_profundidade(no):
        visitados.add(no)

        for vizinhos in grafo[no]:
            if vizinhos not in visitados:
                busca_em_profundidade(vizinhos)

        pilha.append(no)

    for no in grafo:
        if no not in visitados:
            busca_em_profundidade(no)

    for x in pilha[::1]:
        yield list(x)
        

    return pilha[::-1]