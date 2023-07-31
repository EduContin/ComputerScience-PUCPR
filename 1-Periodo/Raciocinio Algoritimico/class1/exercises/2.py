# Algoritimo para calcular valor a ser pago por um cliente em X dias de locacao de um carro

dias = input("Digite a quantidade de dias de locação: ")
preco = 100

valorTotal = preco * int(dias)

print("O cliente deve pagar: R$" + str(valorTotal) + ".")