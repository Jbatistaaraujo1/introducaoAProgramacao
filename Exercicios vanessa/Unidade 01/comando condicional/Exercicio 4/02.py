#Entradas
tipoAparelho = str.lower(input("Escreva o tipo do aparelho: "))
modeloAparelho = str.lower(input("Escreva o modelo do aparelho: "))
quantidadeAparelho = int(input("Escreva a quantidade de aparelhos: "))
#Valores
celSamsung = 921.40
celMotorola = 879.18
tableSamsug = 417.72
tableMultilaser = 339.50

if (tipoAparelho == "celular"):
    if (modeloAparelho == "samsung"):
        valor = celSamsung * quantidadeAparelho
        print(f"o valor da compra foi de R$ {valor:.2f}")
    elif (modeloAparelho == "motorola"):
        valor = celMotorola * quantidadeAparelho
        print(f"o valor da compra foi de R$ {valor:.2f}")
    else:
        print("Marca inexistente")
elif(tipoAparelho == "tablet"):
    if (modeloAparelho == "samsung"):
        valor = tableSamsug * quantidadeAparelho
        print(f"o valor da compra foi de R$ {valor:.2f}")
    elif (modeloAparelho == "multilaser"):
        valor = tableMultilaser * quantidadeAparelho
        print(f"o valor da compra foi de R$ {valor:.2f}")
    else:
        print("Tipo inexistente")
