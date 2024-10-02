import bibLetras
quantVogais = 0
for i in range(6):
    letras = str.upper(input("Digite um letra: "))
    if bibLetras.testeVogal(letras) == True:
        quantVogais += 1
print(quantVogais)