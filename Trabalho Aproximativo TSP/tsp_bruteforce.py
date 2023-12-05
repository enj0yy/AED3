import itertools
import time

def ler_grafo(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph


def brute_force_tsp(grafo):
    vertices = len(grafo)

    custo_minimo = float('inf')
    melhor_caminho = None

    for caminho in itertools.permutations(range(1, vertices)):
        caminho_atual = (0,) + caminho + (0,)
        custo_atual = 0

        for i in range(vertices):
            custo_atual += grafo[caminho_atual[i]][caminho_atual[i + 1]]

        if custo_atual < custo_minimo:
            custo_minimo = custo_atual
            melhor_caminho = caminho_atual

    return list(melhor_caminho), custo_minimo


if __name__ == '__main__':
    start = time.time()

    grafo = ler_grafo("./tsp2_1248.txt")

    caminho, custo = brute_force_tsp(grafo)
    
    print("Melhor caminho:", caminho)
    print("Custo minimo:", custo)

    end = time.time()
    print("Tempo de execucao:", end - start)
