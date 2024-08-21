parcial = 500
total = 800
totalClientes = 2
quantClientes = 0
quantFemino = 0
totalArrecadado = 0
quantIdoso = 0
somaIdoso = 0
while (quantClientes < totalClientes):
    idade = int(input("Escreva a idade: "))
    sexo = str.lower(input("Sexo: Masculino ou Feminino? "))
    tipo = str.lower(input("Tipo: Parcial ou Total? "))
    if (tipo == "parcial"):
        if (sexo == "feminino"):
            if (idade >= 18) and (idade <= 24):
                valor = parcial - (parcial*0.05)
                totalArrecadado += valor
            elif(idade >= 25) and (idade <= 55):
                valor = parcial - (parcial*0.05)
                totalArrecadado += valor
            elif(idade >= 56) and (idade <= 120):
                valor = (parcial*0.09) + parcial
                totalArrecadado += valor
                quantIdoso +=1
                somaIdoso += idade
            quantFemino +=1
        else:
            if(idade >= 18) and (idade <= 24):
                valor = (parcial*0.07) + parcial
                totalArrecadado += valor
            elif(idade >= 25) and (idade <= 55):
                valor = total
                totalArrecadado += valor
            elif(idade >= 56) and (idade <= 120):
                valor = total
                totalArrecadado += valor
                quantIdoso += 1
                somaIdoso += idade
            
    else:
        if (sexo == "feminino"):
            if (idade >= 18) and (idade <= 24):
                valor = total - (total*0.05)
                totalArrecadado += valor
            elif(idade >= 25) and (idade <= 55):
                valor = total - (total*0.05)
                totalArrecadado += valor
            elif(idade >= 56) and (idade <= 120):
                valor = (total*0.09) + total
                totalArrecadado += valor
                quantIdoso += 1
                somaIdoso += idade
            quantFemino += 1
        else:
            if(idade >= 18) and (idade <= 24):
                valor = (total*0.07) + total
                totalArrecadado += valor
            elif(idade >= 25) and (idade <= 55):
                valor = total
                totalArrecadado += valor
            elif(idade >= 56) and (idade <= 120):
                valor = total
                totalArrecadado += valor
                quantIdoso += 1
                somaIdoso += idade
    print(valor)
    quantClientes += 1
if quantIdoso > 0:
    mediaIdoso = somaIdoso // quantIdoso
else:
    mediaIdoso = "Não há idosos"
print(quantFemino)
print(mediaIdoso)
print(totalArrecadado)