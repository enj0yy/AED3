import itertools
import time
import os


def held_karp(dists):
    
    n = len(dists)

    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph


if __name__ == '__main__':
    start = time.time()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "tsp5_27603.txt")
    grafo = read_graph_from_file(file_path)

    min_cost, best_path = held_karp(grafo)
    
    print("Melhor caminho (Held Karp):", best_path)
    print("Custo minimo (Held Karp):", min_cost)

    end = time.time()
    print("Tempo de Execucao: " + str(end - start))
