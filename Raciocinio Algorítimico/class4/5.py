# Escreva um programa que receba 10 números do teclado e exiba a quantidade de números pares e ímpares lidos.

counter = 0
impar = 0
par = 0

while counter < 10:
    num = int(input("Digite um número: "))
    counter  += 1

    if (num % 2) == 0:
        par += 1
    else:
        impar += 1

print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares : {impar}")