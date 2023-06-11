# Escreva um programa que crie uma lista de palavras e imprima a palavra mais
# longa e a palavra mais curta da lista.
import random

palavrasSoltas = ["banana", "morango", "uva", "maracuja", "melancia"]
palavrasEscolhidas = []

for i in range(0, random.randint(3,5)):
    palavrasEscolhidas.append(random.choice(palavrasSoltas))

print(palavrasEscolhidas)

palavrasLen = [len(i) for i in palavrasEscolhidas]
print(palavrasLen)

maiorIndex = max(palavrasLen)
print(f"Maior: {max(palavrasLen)}")

print(f"Menor: {min(palavrasLen)}")
