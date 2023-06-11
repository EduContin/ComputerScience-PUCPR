# Introduction - Python #1 lession

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu Telefone: ")
anoDeNascimento = int(input("Digite seu Ano de Nasciemento: "))

print("Nome: " + nome)
print(f"CPF Formatado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")
print("Telefone: " + str(telefone))
print("Ano de Nascimento: " + str(anoDeNascimento))