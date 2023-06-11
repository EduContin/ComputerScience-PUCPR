# Calcular IMC

peso = float(input("Digite o seu peso corporal: "))
altura = float(input("Digite a sua altura: "))

calculo = peso / (altura ** 2)
imc = str(calculo)
print("Seu IMC é: " + imc[:4])