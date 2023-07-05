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