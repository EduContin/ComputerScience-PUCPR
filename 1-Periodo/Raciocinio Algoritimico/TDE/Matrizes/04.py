# Leia uma matriz 4 x 4, imprima a matriz e retorne a localização
# (linha e a coluna) do maior valor.

matriz = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [7, 8, 9, 10],
    [7, 4, 6, 21]
]

def encontrar_maior(matriz):
    maior = 0
    for linha in matriz:
        if maior < max(linha):
            maior = max(linha)
    
    return maior


maior = encontrar_maior(matriz)
print(maior)
