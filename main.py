import numpy as np

A = np.array([[0.8, 0.2, 0.0], [0.2, 0.0, 0.8], [0.7, 0.2, 0.1]])


def markov_move(A, s):
    n, u, accum = 0, np.random.uniform(0, 1), A[s][0]

    while u > accum:
        n += 1
        accum += A[s][n]

    return n


def principal():
    runs = 1000
    s = 0
    tam = A[0].size
    vet_cont = np.zeros(tam)

    for i in range(runs):
        s = markov_move(A, s)
        vet_cont[s] += 1

    for i in range(tam):
        print(vet_cont[i] / runs)


def questaob():
    runs = 100000
    tam = A[0].size
    vet_cont = np.zeros(tam)
    ocorrencia = 0

    for i in range(runs):
        s = 2
        for j in range(3):
            s = markov_move(A, s)
        if s == 1:
            ocorrencia += 1
    
    print(f'Probabilidade = {ocorrencia/runs}')
    
questaob()
