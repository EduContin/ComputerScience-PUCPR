# Algorítimo que recebe input Celsius e da o output em Fahrenheit.

celsius = float(input("Digite a temperatura em Celcius: "))

fahrenheit = str((celsius * (9 / 5)) + 32)

print(f"A temperatura em Fahrenheit é: {fahrenheit[:4]}")