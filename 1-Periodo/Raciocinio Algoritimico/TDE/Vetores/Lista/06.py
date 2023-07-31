# Faça um programa que receba do usuario um vetor com 10 posições. 
# Em seguida deverá ser impresso o maior e o menor elemento do vetor.

numeros = []

def preencher_lista_10(lista):
    for i in range(10):
        lista.append(int(input(f"Digite o {i + 1}° valor: ")))

preencher_lista_10(numeros)

print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")