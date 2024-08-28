cont = 0
paresPositivos = 0

while (cont < 20):
    numero = int(input("Digite um número: "))
    if (numero >= 0) and (numero % 2 == 0):
        paresPositivos += 1
    cont += 1
print(f"A quantidade de números pares e positivos foi de :{paresPositivos}")
