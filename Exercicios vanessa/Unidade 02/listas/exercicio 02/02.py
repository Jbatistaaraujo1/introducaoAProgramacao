import random

quantNumeros = 10
lista = []

numero = [random.randint(1,100) for i in range(quantNumeros)]
lista.append(numero)

menorNumero = 0
quantImpar = 0
for i in range(quantNumeros):
    if lista[i] < menorNumero:
        menorNumero = lista[i]
    if lista[i] % 2 != 0:
        quantImpar += 1
soma = lista[0]+lista[1]+lista[2]+lista[3]+lista[4]

print(lista)
print(f"Primeiro elemento: {lista[0]} , Último elemento: {lista[9]}")
print(f"A soma dos 5 primeiros elementos: {soma}")
print(f"O menor elemento: {menorNumero}")
print(f"A quantidade de elementos Ímpares: {quantImpar}")