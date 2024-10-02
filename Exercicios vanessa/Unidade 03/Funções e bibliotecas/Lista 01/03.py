import bibNumeros

quant = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    if bibNumeros.testaMultiplo4(numero) == True:
        quant += 1
print(quant)

