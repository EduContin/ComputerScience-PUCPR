# Algorítimo para calcular media de X notas com ou sem Y pesos diferentes.

# Important values set
notas = []
soma = 0

# Asks grades quantity + if has different weight
quantity = int(input("Digite a quantidade de notas (Ex: 4): "))
calcType = input("As notas tem pesos diferentes? (Sim/Nao): ")

# If has different weight
if calcType == "Sim":
    for i in range(quantity): # Asks every grade info
        nota = float(input(f"Digite a {i}° nota: "))

        peso = float(input(f"Digite o peso da sua {i}° nota (Ex: 7): "))

        notas.append(nota * peso) # + every grande in a single var

# If doesn't have different weight
elif calcType == "Nao":
    for i in range(quantity): # Asks every grade info
        nota = float(input(f"Digite a {i}° nota: "))

        notas.append(nota)

else: # In case of incorrect inputs
    print("Confira se escrever 'Sim' ou 'Nao', exatamente, com letra maiuscula no inicio e sem acento.")

# For grade in grades
for nota in notas:
    soma += nota

# OUTPUTS
media = soma / quantity
print(f"[ + ] A média das suas {quantity} notas é: {media}")

# Average checker. If 18 >: SUCCESSs. If not: FAILURE print.
if media >= 7:
    print("## Sua média foi maior que 7. Parabéns você foi APROVADO!")
else:
    print("## Sua média foi menor que 7, você foi REPROVADO.")