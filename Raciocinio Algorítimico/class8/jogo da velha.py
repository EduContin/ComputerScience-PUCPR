import os

# Lógica para finalizar o jogo
shouldStop = False

# Pontuação dos jogadores
jogador1 = 0
jogador2 = 0

# Matriz para criar o tabuleiro
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Clear console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Print do tabuleiro no console
def displayTabuleiro():
    print(f"""
     {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}
    -----------
     {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}
    -----------
     {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}
    """)

def gameCalc():
    
    # Check de linhas horizontais
    for y in range(3):
        if tabuleiro[y][0] == tabuleiro[y][1] == tabuleiro[y][2]:

            if tabuleiro[y][0] == "X":
                print(f"PLAYER 1 Ganhou HORIZONTAL! {y}")
                return "stop"
            
            elif tabuleiro[y][0] == "O":
                print(f"PLAYER 2 Ganhou HORIZONTAL! {y}")
                return "stop"
        
        if tabuleiro[0][y] == tabuleiro[1][y] == tabuleiro[2][y]:

            if tabuleiro[0][y] == "X":
                print(f"PLAYER 1 Ganhou VERTICAL! {y}")
                return "stop"
            
            elif tabuleiro[0][y] == "O":
                print(f"PLAYER 2 Ganhou VERTICAL! {y}")
                return "stop"
        
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:

            if tabuleiro[0][0] == "X":
                print(f"PLAYER 1 Ganhou DIAGONAL 1! {y}")
                return "stop"
            
            elif tabuleiro[0][0] == "O":
                print(f"PLAYER 2 Ganhou DIAGONAL 1! {y}")
                return "stop"

        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:

            if tabuleiro[0][2] == "X":
                print(f"PLAYER 1 Ganhou DIAGONAL 2! {y}")
                return "stop"
            
            elif tabuleiro[0][2] == "O":
                print(f"PLAYER 2 Ganhou DIAGONAL 2! {y}")
                return "stop"
# Lógica do Menu
while True:

    clear()

    # Jogada do PLAYER 1
    while True:
        displayTabuleiro()

        playY1 = int(input("Digite a linha da sua jogada (1 a 3): ")) - 1
        playX1 = int(input("Digite a coluna da sua jogada (1 a 3): ")) - 1

        if tabuleiro[playY1][playX1] == " ":
            tabuleiro[playY1][playX1] = "X"
            clear()
            displayTabuleiro()
            break
        else:
            clear()
            print("\nPosição ocupada. Jogue novamente!")

    clear()

    if gameCalc() == "stop":
        break

    # Jogada do PLAYER 2
    while True:
        displayTabuleiro()

        playY2 = int(input("Digite a linha da sua jogada (1 a 3): ")) - 1
        playX2 = int(input("Digite a coluna da sua jogada (1 a 3): ")) - 1

        if tabuleiro[playY2][playX2] == " ":
            tabuleiro[playY2][playX2] = "O"
            clear()
            displayTabuleiro()
            break
        else:
            clear()
            print("\nPosição ocupada. Jogue novamente!")
    

    if gameCalc() == "stop":
        break