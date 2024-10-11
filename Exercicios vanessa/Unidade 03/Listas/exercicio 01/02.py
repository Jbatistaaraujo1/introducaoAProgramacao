import bibliotecalistas

numeros = int(input("Escreva a quantidade de numeros da lista: "))
valor = int(input("Escreva o valor que vai multiplicar a lista: "))
lista = []
for i in range(numeros):
    num = int(input(f"Escreva o {i}º número: "))
    lista.append(num)
print(bibliotecalistas.multiplicaLista(lista, valor))