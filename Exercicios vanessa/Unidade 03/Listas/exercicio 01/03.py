import bibliotecalistas

numeros = int(input("Escreva a quantidade de números da lista: "))
valor = int(input("Escreva o valor a ser buscado na lista: "))
lista = []
for i in range(numeros):
    num = int(input(f"Escreva o {i}º número: "))
    lista.append(num)
print(bibliotecalistas.Busca(lista, valor))
