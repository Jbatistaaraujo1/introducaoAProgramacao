lista = []
quantNumeros = 5
for cont in range(quantNumeros):
    numero = int(input("Escreva um número: "))
    lista.append(numero)

novaLista = []
for i in range(quantNumeros - 1):
    novoNumero = lista[i] + lista[i + 1]
    novaLista.append(novoNumero)

novaLista.append(len(lista) - 1)

print(lista)
print(novaLista)