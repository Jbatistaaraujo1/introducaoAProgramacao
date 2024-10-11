import bibliotecalistas

numeros = int(input("Escreva a quantidade de numeros da lista: "))
valor = int(input("escreva o valor a ser buscado: "))
lista = []
for i in range(numeros):
    num = int(input(f"Escreva o {i}º número: "))
    lista.append(num)
print(bibliotecalistas.ContaOcorrencias(lista, valor))
