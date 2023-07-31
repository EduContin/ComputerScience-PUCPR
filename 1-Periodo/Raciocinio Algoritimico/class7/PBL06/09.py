# Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
# suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
# uma determinada letra e informe se ele acertou ou errou.
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t" ,"u", "v", "w", "x", "y", "z"]

random.shuffle(letras)
letra = random.choice(letras)
indiceDaLetra = letras.index(letra)

aposta = int(input(f"Advinhe a posição da letra {letra}: "))

if aposta == indiceDaLetra:
    print("Você acertou!")
else:
    print(f"Você errou. A posição era {indiceDaLetra}.")