# Implemente um prorgama em Python para imprimir na tela ao somatório dos N primeiros
# números inteiros a partir do 1.
# Sendo N lido do teclado

num = int(input("Digite um número: "))
counter = 1
soma = 0

while counter != (num + 1):
    soma += counter
    counter += 1

print(f"A soma é: {soma}")