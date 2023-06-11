# Dado um vetor A de tamanho N e um vetor B de tamanho N, crie um programa
# que calcule a soma dos elementos desses vetores e armazene o resultado em
# um vetor C de tamanho N. Regras:
# a. O tamanho dos vetores A, B e C é fornecido pelo usuário.
# b. Os elementos dos vetores A e B são fornecidos pelo usuário.
# c. A soma dos elementos de A[i] e B[i] deve ser armazenada em C[i].
# d. O vetor C deve ser exibido na tela após o cálculo.

N = int(input("Digite o tamanho dos vetores: "))

vetorA = [0] * N
vetorB = [0] * N
vetorC = [0] * N

for i in range(0, N):
    vetorA[i] = int(input(f"Valor do vetor A, posição {i}: "))
    vetorB[i] = int(input(f"Valor do vetor B, posição {i}: "))

    vetorC[i] = vetorA[i] + vetorB[i]
    print(f"Soma na posição {i} = {vetorC[i]}")

print(f"Vetor das somas: {vetorC}")