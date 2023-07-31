# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
# elementos. Escreva ao final a matriz obtida

matriz = [
    [7, 5, 4, 1, 9],
    [1, 0, 3, 1, 2],
    [9, 8, 7, 6, 5],
    [1, 3, 2, 8, 6],
    [4, 6, 4, 6, 3]
]

def criar_diagonal():
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if x == y:
                matriz[y][x] = 1
            else:
                matriz[y][x] = 0

def print_matriz():
    for linha in matriz:
        print(linha)

def logic():
    criar_diagonal() # Limpa a matriz com 0's e senha a diagonal principal com 1's
    print() # Print de todas linhas da matriz formatado

logic()