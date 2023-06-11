# Faça um programa que preenche um vetor de 50 posições com valores
# aleatórios entre 0 e 20 e encontre:
# Obs: Para fazer um vetor de tamanho 50 preenchido com 0 é possível fazer:
# vetor = [0] * 50. Note que o valor 50 também pode ser substituído por uma variável
# qualquer.
# a. A soma dos valores armazenados no vetor.
# b. O número de ocorrências do valor 9.
# c. O maior valor armazenado no vetor.
# d. O menor valor armazenado no vetor.

# Importando as bibliotecas necessárias
import random

# Variável para auxiliar na inserção de valores no vetor
index = 0
soma = 0
noves = 0
maior = 0
menor = 0

# Criando o vetor com 50 posições
vetor = [0] * 50

while index < 50:
    # Gera um valor de 0 a 20
    vetor[index] = random.randint(0, 20)

    # Cria uma soma de todos vetores
    soma += vetor[index]

    # Conta quantos 9 apareceram no vetor
    if vetor[index] == 9:
        noves += 1

    # Maior valor do vetor
    if vetor[index] > maior:
        maior = vetor[index]

    # Maior valor do vetor
    if vetor[index] < menor:
        menor = vetor[index]

    # Lógica de loop
    index += 1


print("Vetor:\n", vetor)
print("A) ", soma)
print("B) ", noves) 
print("C) ", maior)
print("D) ", menor)


index = 0
