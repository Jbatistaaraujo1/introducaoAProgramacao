ano = int(input("Escreva um ano: "))
quantBissextos = 0
while (ano >0) :
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0): 
        quantBissextos += 1
    ano = int(input("Escreva outro ano: "))
print(quantBissextos)

