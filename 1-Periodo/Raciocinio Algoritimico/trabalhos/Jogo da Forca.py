import random

# Vetor com as palavras secretas
vetorTodasPalavras = ["uva", "melancia", "banana"]

# Escolher uma palavra secreta
palavra = random.choice(vetorTodasPalavras)
print(palavra)

# Variáveis de setup
errors = 0
posicao = 0
tamanhoDaPalavra = 0
tentativas = 6

# Sistema para descobrir o tamanho do vetor
for letra in palavra:
    tamanhoDaPalavra += 1

# Vetor com as letras censuradas
vetorDisplay = ["_"] * tamanhoDaPalavra

# MENU
while True:
    # Display de informações
    print(f"\nTENTATIVAS RESTANTES: {tentativas}")
    print(" ".join(vetorDisplay))

    # Jogada
    letraInput = input("\nDigite uma letra: ")

    # Verificador/Contador de erros/acertos
    if letraInput in palavra:
        for letra in palavra:
            if letraInput == letra:
                vetorDisplay[posicao] = letra # Adiciona a letra no acerto
                posicao += 1
            else:
                posicao += 1
    else:
        tentativas -= 1

    # Saída em caso de derrota
    if tentativas == 0:
        print("\nVocê PERDEU!\n")
        break

    # Saída em caso de vitória
    if "_" not in vetorDisplay:
        print(f"\nVOCÊ GANHOU!\n A palavra era: {palavra}")
        break

    posicao = 0 # Reseta para descobrir a index da próxima letra