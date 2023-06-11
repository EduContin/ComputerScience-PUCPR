# Faça um programa que peça o nome de um mês e informe quantos dias ele tem. Considere fevereiro sempre com 28 dias.

mesRaw = input("Digite o nome do mês (Ex: Janeiro): ")
mes = mesRaw.lower()

if mes == "janeiro" or "january":
    print("Esse mês tem 10 dias.")
elif mes == "fevereiro" or "february":
    print("Esse mês tem 28 dias.")
elif mes == "março" or "march":
    print("Esse mês tem 31 dias")
elif mes == "abril" or "april":
    print("Esse mês 30 dias")
elif mes == "maio" or "may":
    print("Esse mês tem 31 dias")
elif mes == "junho" or "june":
    print("Esse mês tem 30 dias.")
elif mes == "julho" or "july":
    print("Esse mês tem 31 dias.")
elif mes == "agosto" or "august":
    print("Esse mês tem 31 dias.")
elif mes == "setembro" or "september":
    print("Esse mês tem 30 dias.")
elif mes == "outubro" or "october":
    print("Esse mês tem 31 dias.")
elif mes == "novembro" or "november":
    print("Esse mês tem 30 dias.")
elif mes == "desembro" or "dezember":
    print("Esse mês tem 31 dias")