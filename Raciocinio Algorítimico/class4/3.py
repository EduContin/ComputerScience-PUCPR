# Implemente um programa em python para ler do teclado números.
# Caso o usuário forneça um número igual a -1, o programa deve fornecer a média dos número e encerrar.

num = 0
soma = 0
counter = 0

while True:

    num = int(input(f"Digite o {counter + 1}° número: "))

    if num == -1:
        break

    counter += 1
    soma += num

media = soma / counter
print(f"A média dos valores é: {media}")