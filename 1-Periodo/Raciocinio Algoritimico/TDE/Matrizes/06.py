# Leia duas matrizes 4 x 4 e escreva uma terceira
# com os maiores valores de cada posição das matrizes lidas.

matrizAlpha = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [7, 8, 9, 10],
    [7, 4, 6, 21]
]

matrizBeta = [
    [7, 0, 1, 1],
    [2, 5, 6, 2],
    [3, 2, 2, 20],
    [12, 6, 4, 2]
]

matrizDelta = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def bind_matriz(matrizA, matrizB):

    if len(matrizA) == len(matrizB):

        for y in range(len(matrizA)):
            for x in range(len(matrizA)):
                if matrizA[y][x] > matrizB[y][x]:
                    matrizDelta[y][x] = matrizA[y][x]
                else:
                    matrizDelta[y][x] = matrizB[y][x]
                    
    else:
        return "ERROR: As matrizes precisam ter o mesmo tamanho."

bind_matriz(matrizAlpha, matrizBeta)

for linha in matrizDelta:
    print(linha)