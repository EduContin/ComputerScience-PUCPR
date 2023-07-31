#  Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

vetorAlpha = [2, 75, 3, 14, 0, 5, 77, 29, 37, 8]

def contar_pares(vetor):
    pares = 0
    for item in vetor:
        if item % 2 == 0:
            pares += 1
    
    return pares

print(f"O vetor tem {contar_pares(vetorAlpha)} números pares.")
