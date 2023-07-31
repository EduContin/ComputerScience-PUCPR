# Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

vetorDelta = [0] * 6

def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i + 1}° valor: "))

preencher_vetor(vetorDelta)
print(vetorDelta)