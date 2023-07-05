from EntradaUser import entrada_do_usuario
from OrdenacaoTopologica import ordenacao_topologica
from VerificadorAciclico import verificacao_grafo_aciclico


"""Grafos de Exemplo"""
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


if __name__ == '__main__':
    grafo = entrada_do_usuario()

    if verificacao_grafo_aciclico(grafo):
        print("O grafo contém ciclos")
    else:
        print("O grafo é acíclico")
        for order in ordenacao_topologica(grafo):
            print(order)
