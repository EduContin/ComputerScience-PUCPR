# Utilizando a mesma matriz da prática anterior, altere os valores ans seguintes posiçoes:
# 1 - [0][0] para 20 | [1][2] para 15 | 3 - [2][1] para 19
# Imrpima novamente a matriz das 3 formas anteriores.

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
        if linha == 0 and coluna == 0:
            matriz[linha][coluna] = 20
        elif linha == 1 and coluna == 2:
            matriz[linha][coluna] = 15
        elif linha == 2 and coluna == 1:
            matriz[linha][coluna] = 19
        print(matriz[linha][coluna])

print(matriz)