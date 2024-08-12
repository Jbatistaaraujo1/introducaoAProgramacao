# Escreva um programa que receba como entrada vários anos, até que seja informado um ano negativo, 
# e exiba quantos anos lidos foram bissextos. (Obs: Há duas possibilidades para 
# um ano ser bissexto: se ele for múltiplo de 400, ou se ele for múltiplo de 4 mas não for múltiplo de 100)

ano = int(input("Escreva um ano: "))
quantBissextos = 0
while (ano >0) :
    if (ano) or (ano // 400 == 0): 
        quantBissextos += 1
    ano = int(input("Escreva outro ano: "))
print(quantBissextos)

