import random

numerosJogador1 = []
numerosJogador2 = []

for i in range(0,3):
    numerosJogador1.append(random.randint(1, 6))
    numerosJogador2.append(random.randint(1, 6))

    resultado1 = sum(numerosJogador1)
    resultado2 = sum(numerosJogador2)

print(f"J1: {resultado1} | J2: {resultado2}")

if resultado1 > resultado2:
    print("Jogador 1 ganhou.")

elif resultado1 < resultado2:
    print("Jogador 2 ganhou.")

else:
    print("Empate.")