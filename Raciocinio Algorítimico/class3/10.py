# Faça um programa que peça um número inteiro e verifique se ele é primo ou não.

number = int(input("Digite um número: "))

count = number - 1
isPrimo = True

for i in range(2, (count -1)):
    if number % i == 0:
        isPrimo = False
    if isPrimo == False:
        print("O número não é primo!")
        break

if isPrimo == True:
    print("O número é primo!")