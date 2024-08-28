quantMultiplos = 0
for cont in range(1,3,1):
    numero = int(input("Escreva um número: "))
    if numero % 4 == 0:
        quantMultiplos += 1
print(f"{quantMultiplos} múltiplos")