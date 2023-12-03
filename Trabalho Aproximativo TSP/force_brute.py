import itertools
import time
import os


def brute_force_tsp(dists):
    n = len(dists)
    all_cities = set(range(n))

    min_cost = float('inf')
    best_path = None

    start_time = time.time()

    # Gera todas as permutações possíveis dos nós
    for path in itertools.permutations(range(1, n)):
        current_path = (0,) + path + (0,)
        current_cost = sum(dists[current_path[i]][current_path[i + 1]] for i in range(n))

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    end_time = time.time()
    elapsed_time = end_time - start_time

    return min_cost, best_path, elapsed_time


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph


if __name__ == '__main__':
    start = time.time()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "tsp3_1194.txt")
    grafo = read_graph_from_file(file_path)

    min_cost_brute, best_path_brute, elapsed_time_brute = brute_force_tsp(grafo)
    
    print("Melhor caminho:", best_path_brute)
    print("Custo minimo:", min_cost_brute)
    print("Tempo de Execucao:", elapsed_time_brute)

    end = time.time()
    print("Tempo total de execucao:", end - start)
