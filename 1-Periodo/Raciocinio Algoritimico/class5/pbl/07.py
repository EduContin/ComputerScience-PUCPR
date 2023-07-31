tamanhoVetor = 15
index = 0
index2 = 0
quantidadeZero = 0

vetor = [0] * tamanhoVetor

while index < 15:
    vetor[index] = int(input("Digite um valor: "))

    index += 1

print(vetor)
index = 0

while index < 15 - quantidadeZero:
    if vetor[index] == 0:
        index2 = index

        while index2 < 14:
            vetor[index2] = vetor[index2 + 1]
            index2 += 1

        vetor[14 - quantidadeZero] = 0
        quantidadeZero += 1

    index += 1
print(vetor)