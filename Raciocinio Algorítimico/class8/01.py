# Crie uma matriz de tamanho 3x3 e preencha-a om valores de 1 a 9.
# Imprima a matriz das três formas:
# 1 - Print(matriz) | 2 - Utilizando 1 for | 3 - Utilizando 2 for's.

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

