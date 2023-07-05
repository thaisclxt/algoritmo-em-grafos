from collections import defaultdict

def entrada_do_usuario():
    grafo = defaultdict(list)

    arestas = int(input("Digite o número de arestas do grafo: "))

    for i in range(arestas):
        aresta = input(f"Digite a aresta {i+1} no formato 'origem destino1 destino2 ... : ")
        origem, *destino = aresta.split()
        grafo[origem].append(destino)

    print(grafo)
    return grafo

