import random
quantNumeros = 10
lista = []

numero = [random.randint(1,100) for i in range(quantNumeros)]
lista.append(numero)

print(lista)