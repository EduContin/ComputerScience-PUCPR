# Faça as segunites operações aritméticas com os valores de casa posição e armazene-as em variáveis:

matriz = [
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 4]
]

# Print único
print(matriz)

# Print com 1 for
for i in range(len(matriz)):
    print(matriz[i])

#print com 2 for's
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):

        print(matriz[linha][coluna])

print(matriz[0][0] + matriz[0][1])
print(matriz[2][2] - matriz[2][1])
