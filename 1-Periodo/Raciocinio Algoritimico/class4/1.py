# Imprima na tela a tabuada de um némero inteiro lido pelo teclado:

num = int(input("Digite um número: "))
counter = 0

while counter <= 10:
    print(f"{num} vezes {counter} =  {num * counter}")
    counter += 1