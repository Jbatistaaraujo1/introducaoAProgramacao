import bibliotecalistas

numero = int(input("Escreva quantos números a lista vai ter: "))
lista = []

for i in range(numero):
    num = int(input(f"{i}º número: "))
    lista.append(num)
if numero == 0:
    print(0)
else:
    print(bibliotecalistas.MediaInteiraLista(lista))
