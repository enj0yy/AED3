import os
import networkx as nx

def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph

def mst_tsp(graph):
    num_nodes = len(graph)

    # Criação de um grafo usando NetworkX
    G = nx.Graph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            G.add_edge(i, j, weight=graph[i][j])

    # Construção da Árvore Geradora Mínima
    mst = nx.minimum_spanning_tree(G)

    # Passeio pré-ordem na Árvore Geradora Mínima
    approx_path = list(nx.dfs_preorder_nodes(mst, source=0))

    # Volta para o primeiro nó
    approx_path.append(approx_path[0])

    # Cálculo do custo total
    approx_cost = sum(graph[approx_path[i]][approx_path[i + 1]] for i in range(num_nodes))

    return approx_path, approx_cost, mst

# Obter o caminho absoluto para o diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho completo para o arquivo de texto na pasta raiz do código
file_path = os.path.join(current_directory, "tsp2_1248.txt")

# Leitura da matriz de adjacência a partir do arquivo
graph_from_file = read_graph_from_file(file_path)

# Resolvendo o TSP usando o algoritmo da Árvore Geradora Mínima
approx_path, approx_cost, mst = mst_tsp(graph_from_file)

print("Caminho aproximado (MST):", approx_path)
print("Custo aproximado (MST):", approx_cost)

