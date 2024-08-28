
continuar = "sim"
quantMultiplos = 0
while (continuar != "não") and (continuar!= "nao"):
    numero = int(input("Escreva um número: "))
    if numero % 3 == 0:
        quantMultiplos += numero
    continuar = str.lower(input("Deseja continuar? sim ou não: "))
print(f"A soma dos multiplos de 3 foi de {quantMultiplos}")