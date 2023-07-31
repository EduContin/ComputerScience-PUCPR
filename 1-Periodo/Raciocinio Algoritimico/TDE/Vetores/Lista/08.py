# Crie um programa que le 6 valores inteiros e, em seguida
# mostre na tela os valores lidos na ordem inversa.

numeros = []

def ler_valores(lista):
    for i in range(6):
        lista.append(int(input("Digite um valor: ")))

ler_valores(numeros)
numeros.reverse()
print(numeros)