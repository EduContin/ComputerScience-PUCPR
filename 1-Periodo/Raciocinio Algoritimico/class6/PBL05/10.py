#Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.

vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
vetorAuxiliar = [0] * 10
repeticoes = -1

for i in range(0, 10):
    repeticoes = -1
    for i2 in range(0, 10):
        if i == i2:
            continue
        else:
            if vetor[i] == vetor[i2]:
                repeticoes += 1
                vetorAuxiliar[repeticoes] = vetor[i]

for num in vetorAuxiliar:
    if num == 0:
        continue
print(vetorAuxiliar)

