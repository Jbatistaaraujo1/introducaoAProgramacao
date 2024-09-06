lista = []
listaMultiplos = []
quantidadeNumeros = 8

for cont in range(quantidadeNumeros):
    numero = int(input("Digite um número: "))
    lista.append(numero)
for i in range(quantidadeNumeros):
    if lista[i] % 3 == 0:
        print(lista[i])