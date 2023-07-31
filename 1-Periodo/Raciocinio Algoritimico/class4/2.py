# Implemente um programa em pyton para ler do teclado a nota de um aluno.
# Verifique se o valor lido é uma nota válido (maior que 7).
# Se não for, er este valor até que a mesma seja válida.

nota = float(input("Digite um número: "))

while nota < 7:
    nota = float(input("Nota inválida. Digite novamente: "))