numeros = int(input("Escreva um número: "))
quantPares = 0
somaPares = 0
while (numeros != 100):
    if (numeros % 2 == 0):
        quantPares += 1
        somaPares = somaPares + numeros
    numeros = int(input("Escreva outro número: "))
if quantPares > 0:
    media = somaPares // quantPares
    print(f"A média dos números pares é {media}")
else:
    print("Não foram lidos números pares")