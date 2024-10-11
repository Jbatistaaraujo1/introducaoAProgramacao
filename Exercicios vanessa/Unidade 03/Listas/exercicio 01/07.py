import bibliotecalistas

numeros = int(input("Escreva a quantidade de números que tem na lista: "))
lista = []
for i in range(numeros):
    num = int(input(f"Escreva o {i}º número: "))
    lista.append(num)
print(bibliotecalistas.TestaOrdenacao(lista))

