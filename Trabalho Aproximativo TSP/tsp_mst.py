import os
import networkx as nx
import time

def ler_grafo(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph

def mst_tsp(grafo):
    vertices = len(grafo)
    
    G = nx.Graph()
    for i in range(vertices):
        for j in range(i + 1, vertices):
            G.add_edge(i, j, weight=grafo[i][j])

    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

    caminho_aproximado = list((nx.dfs_preorder_nodes(mst, source=0)))
    caminho_aproximado.append(0)

    custo_aproximado = 0
    for i in range(vertices):
        custo_aproximado += grafo[caminho_aproximado[i]][caminho_aproximado[i + 1]] 
    
    return caminho_aproximado, custo_aproximado

if __name__ == '__main__':
    start = time.time()

    grafo = ler_grafo("./tsp1_253.txt")

    caminho_aproximado, custo_aproximado = mst_tsp(grafo)

    print("Caminho aproximado (MST):", caminho_aproximado)
    print("Custo aproximado (MST):", custo_aproximado)

    end = time.time()
    print("Tempo de Execucao: " + str(end - start))

