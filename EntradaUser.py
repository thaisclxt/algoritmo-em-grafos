from collections import defaultdict

def entrada_do_usuario():
    grafo = {}

    arestas = int(input("Digite o número de arestas do grafo: "))

    for i in range(arestas):
        aresta = input(f"Digite a aresta {i+1} no formato 'origem destino1 destino2 ...': ")
        origem, *destinos = aresta.split()
        grafo[origem] = destinos
    return grafo

