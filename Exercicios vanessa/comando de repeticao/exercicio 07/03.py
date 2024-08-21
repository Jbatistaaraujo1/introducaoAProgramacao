parcial = 500
total = 800
totalClientes = 300
quantClientes = 0
quantFemino = 0
totalArrecadado = 0

while (quantClientes < totalClientes):
    idade = int(input("Escreva a idade: "))
    sexo = str.lower(input("Sexo: Masculino ou Feminino? "))
    tipo = str.lower(input("Tipo: Parcial ou Total? "))
    if (tipo == "parcial"):
        if (sexo == "feminino"):
            if (idade >= 18) and (idade <= 24):
                valor = parcial - (parcial*0.05)
            elif(idade >= 25) and (idade <= 55):
                valor = parcial - (parcial*0.05)
            elif(idade >= 56) and (idade <= 120):
                valor = (parcial*0.09) + parcial
        else:
            if(idade >= 18) and (idade <= 24):
                valor = (parcial*0.07) + parcial
            else:
                valor = parcial
    else:
        if (sexo == "feminino"):
            if (idade >= 18) and (idade <= 24):
                valor = parcial - (parcial*0.05)
            elif(idade >= 25) and (idade <= 55):
                valor = parcial - (parcial*0.05)
            elif(idade >= 56) and (idade <= 120):
                valor = (parcial*0.09) + parcial
        else:
            if(idade >= 18) and (idade <= 24):
                valor = (parcial*0.07) + parcial
            else:
                valor = parcial
                