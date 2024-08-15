sair = "não"
quantGratuitos = 0
while sair != "sim":
    idade = int(input("Escreva a sua idade: "))
    if (idade <= 10) or (idade >60):
        quantGratuitos += 1

    sair = str.lower(input("Deseja sair do programa? Digite sim ou não: "))
print(f"A quantidade de pessoas com ingresso gratuito foi {quantGratuitos}")