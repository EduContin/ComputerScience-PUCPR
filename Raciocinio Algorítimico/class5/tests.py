# Implemente um programa em Python para verificar quantos números
# uma aposta acertou na Mega Sena. O programa deve ler do teclado
# os 6 números apostados e comparar com os 6 números sorteados.
# Ao final, o programa deve exibir os números sorteados, números
# jogados e quantidade de acertos.

import random

index = 0
index2 = 0
acertos = 0

apostas = [0, 0, 0, 0 ,0 ,0]
megasena = [0, 0, 0, 0, 0, 0]

while index != 6:
    # Input da aposta
    apostas[index] = int(input("Digite uma aposta: "))

    # Gerador de valores da MegaSena
    megasena[index] = random.randint(1, 60)

    index += 1

index = 0

while index != 6:
    while index2 != 6:
        if apostas[index] == megasena[index2]:
            acertos += 1
        index2 += 1
    index += 1
    index2 = 0

# if apostas[0] in megasena:
#     acertos += 1
# if apostas[1] in megasena:
#     acertos += 1
# if apostas[2] in megasena:
#     acertos += 1
# if apostas[3] in megasena:
#     acertos += 1
# if apostas[4] in megasena:
#     acertos += 1
# if apostas[5] in megasena:
#     acertos += 1

print(megasena)
print(apostas)
print(acertos)