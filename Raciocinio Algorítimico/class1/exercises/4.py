# Algorítimo para calcular media de X notas com ou sem Y pesos diferentes.
notas = []
soma = 0

quantity = int(input("Digite a quantidade de notas (Ex: 4): "))
calcType = input("As notas tem pesos diferentes? (Sim/Nao): ")
if calcType == "Sim":
    for i in range(quantity):
        nota = float(input(f"Digite a {i}° nota: "))

        peso = float(input(f"Digite o peso da sua {i}° nota (Ex: 7): "))

        notas.append(nota * peso)
elif calcType == "Nao":
    for i in range(quantity):
        nota = float(input(f"Digite a {i}° nota: "))

        notas.append(nota)
else:
    print("Confira se escrever 'Sim' ou 'Nao', exatamente, com letra maiuscula no inicio e sem acento.")

print(notas)
for nota in notas:
    soma += nota

media = soma / quantity
print(f"A média das suas {quantity} notas é: ")