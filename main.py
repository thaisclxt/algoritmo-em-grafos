def verificacao_grafo_aciclico(grafo):
    nos_visitados = set()
    pilha_recursiva = set() # Está pilha recursiva serve para indicar que o nó foi visitado em um caminho atual e aninda não foi concluido

    def busca_em_profundidade(no):
        nos_visitados.add(no)
        pilha_recursiva.add(no)

        for vizinho in grafo[no]:
            if vizinho not in nos_visitados:
                if busca_em_profundidade(vizinho):
                    return True
            elif vizinho in pilha_recursiva:
                return True

        pilha_recursiva.remove(no)
        return False

    for no in grafo:
        if no not in nos_visitados:
            if busca_em_profundidade(no):
                return True

    return False

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
    resultado = pilha[::-1]
    print(resultado)
    return pilha[::-1]



GrafoAciclico = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F'],
    'F': []
}

GrafoContendoCiclo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F'],
    'F': ['A']
}

if verificacao_grafo_aciclico(GrafoAciclico):
    print("O gráfico contém ciclos")
else:
    print("O gráfico é acíclico")
    ordenacao_topologica(GrafoAciclico)