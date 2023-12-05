import itertools
import time

def ler_grafo(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph

def held_karp(grafo):
    vertices = len(grafo)

    C = {}

    # Define o custo de transição a partir do estado inicial
    for k in range(1, vertices):
        C[(1 << k, k)] = (grafo[0][k], 0)

    # Itera sobre subconjuntos de tamanho crescente e armazena resultados intermediários
    # de maneira clássica de programação dinâmica
    for subset_size in range(2, vertices):
        for subset in itertools.combinations(range(1, vertices), subset_size):
            # Configura os bits para todos os nós neste subconjunto
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Encontra o custo mais baixo para chegar a este subconjunto
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + grafo[m][k], m))
                C[(bits, k)] = min(res)

    # Estamos interessados em todos os bits, exceto o menos significativo (o estado inicial)
    bits = (2**vertices - 1) - 1

    # Calcula o custo ótimo
    res = []
    for k in range(1, vertices):
        res.append((C[(bits, k)][0] + grafo[k][0], k))
    custo, parent = min(res)

    # Retrocede para encontrar o caminho completo
    caminho = [0]
    for i in range(vertices - 1):
        caminho.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    caminho.append(0)

    return list(reversed(caminho)), custo


if __name__ == '__main__':
    start = time.time()

    grafo = ler_grafo("./tsp4_7013.txt")

    caminho, custo = held_karp(grafo)
    
    print("Melhor caminho (Held Karp):", caminho)
    print("Custo minimo (Held Karp):", custo)

    end = time.time()
    print("Tempo de Execucao: " + str(end - start))
