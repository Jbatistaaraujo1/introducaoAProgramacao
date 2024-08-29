quantMultiplos = 0
numero1 = int(input("Escreva um número: "))
numero2 = int(input("Escreva um número: "))
if numero1 > numero2:
    for cont in range(numero1 + 1,numero2,1):
        if cont % 4 == 0:
            quantMultiplos += 1
print(f"{quantMultiplos} múltiplos")