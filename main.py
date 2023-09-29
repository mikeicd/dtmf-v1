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

def parte2():
    runs = 100000
    passo = 0.2
    segundos = runs*passo
    tam = A[0].size
    vet_cont = np.zeros(tam)
    soma = 0
    tranf_bts = [10, 100, 1000]
    s = 0
    for i in range(runs):
        s = markov_move(A, s)
        soma += tranf_bts[s]
    
    print(f'Vazão = {soma/segundos}')


def parte3():
    # Variável para rastrear o tempo total 
    total_time_in_state  = 0
    runs = 100000
    passo = 0.2
    segundos = runs * passo
    tam = A[0].size
    vet_cont = np.zeros(tam)
    s = 0
    # Variável para rastrear a duração do estado de transmissão de pacote de tamanho 1000
    state_duration = 0  

    for i in range(runs):
        s = markov_move(A, s)
        state_duration += 1
        vet_cont[s] += 1
        # Se o estado atual é o estado de transmissão de pacote de tamanho 1000
        if s == 2:  
            # Adiciona o tempo de passo no tempo total no estado
            total_time_in_state += passo  
    #print(f'{vet_cont[0]} / {vet_cont[1]} / {vet_cont[2]}')
    # Cálculo da vazão
    vazao = vet_cont[2] * 1000 / state_duration  
    print(f'Vazão = {vazao}')
    print(f'Tempo médio de estadia no estado de transmissão de pacote de tamanho 1000 = {total_time_in_state / vet_cont[2]} épocas')
    
#questaob()

parte3()
