continuar = "sim"
quantGratuitos = 0
while (continuar != "não") and (continuar != "nao"):
    idade = int(input("Escreva a sua idade: "))
    if (idade <= 10) or (idade >60):
        quantGratuitos += 1

    continuar = str.lower(input("Deseja continuar? Digite sim ou não: "))
print(f"A quantidade de pessoas com ingresso gratuito foi {quantGratuitos}")