# Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a media dos valores.

numeros = []

def preencher_lista_5(lista):
    for i in range(5):
        lista.append(int(input("Digite um valor: ")))
    
def media(lista):
    soma = 0
    for item in lista:
        soma += item
        
    media = soma / len(lista)
    return media

preencher_lista_5(numeros)

print("Maior: ", max(numeros))
print("Menor: ", min(numeros))
print("Média: ", media(numeros))