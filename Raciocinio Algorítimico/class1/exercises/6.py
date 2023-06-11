# Calcular preço de produto vendido por kilo

# Inputs
peso = float(input("Digite o peso em gramas [g] (Ex: 2500): "))
preco = float(input("Digite o preço por Kilo (Ex: 75): "))

# Transforma o peso em gramas para kilo
pesoFinal = peso / 1000

# Multiplica a quantidade em kilos pelo preço por kilo
valorFinal = pesoFinal * preco

# Outputs o valor a ser pago
print(f"O valor final é: {valorFinal}")