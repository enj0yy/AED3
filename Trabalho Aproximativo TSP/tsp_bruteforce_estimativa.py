import itertools
import time
import math

def ler_grafo(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = [list(map(int, line.split())) for line in lines]
    return graph

def brute_force_tsp_estimative(grafo, maximo_iteracoes):
    iteracoes = 0
    start = time.time()
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

        iteracoes += 1
        if iteracoes == maximo_iteracoes:
            break
    
    end = time.time()
    print("Tempo de ", iteracoes, " iteracoes:", end - start)

    tempo_estimado = ((math.factorial(vertices-1)/maximo_iteracoes) * (end-start))
    print("Tempo estimado (segundos): ", tempo_estimado)

    tempo_estimado = tempo_estimado/60  # em minutos
    print("Tempo estimado (minutos): ", tempo_estimado)

    tempo_estimado = tempo_estimado/60  # em horas
    print("Tempo estimado (horas): ", tempo_estimado)

    tempo_estimado = tempo_estimado/24  # em dias
    print("Tempo estimado (dias): ", tempo_estimado)

    tempo_estimado = tempo_estimado/365  # em anos
    print("Tempo estimado (anos): ", tempo_estimado)

            
if __name__ == '__main__':
    grafo = ler_grafo("./tsp5_27603.txt")
    brute_force_tsp_estimative(grafo,1000000)

    
    
