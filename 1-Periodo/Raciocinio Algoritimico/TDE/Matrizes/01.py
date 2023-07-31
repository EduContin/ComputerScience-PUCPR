# Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui

matriz = [
    [4, 11, 3, 77],
    [22, 9, 13, 8],
    [1, 7, 2, 101],
    [0, 31, 21, 9]
]

def contar_maiores_10(matriz):
    maioresQue10 = 0
    
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if matriz[x][y] > 10:
                maioresQue10 += 1
    return maioresQue10

print(f"Maiores que 10:  {contar_maiores_10(matriz)}")

