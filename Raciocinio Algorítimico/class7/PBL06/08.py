# Escreva um programa que crie uma lista com os números de 1 a 10 elevados ao
# quadrado. Em seguida, calcule a soma dos elementos da lista e imprima o
# resultado.

import random

numeros = [] 

for i in range(0, 10):

    numeros.append(random.randint(0, 10) ** 2)

print(numeros)
print(sum(numeros))