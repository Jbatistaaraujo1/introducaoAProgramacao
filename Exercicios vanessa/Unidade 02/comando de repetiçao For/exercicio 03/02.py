peca = 7
quilo = 5
seco = 3.50
totalArrecadado = 0
quantSeco = 0
for cont in range(1,51):
    tipo = str.lower(input("Escreva o tipo de cobrança: "))
    if tipo == "peça":
        quantPecas = int(input("Escreva a quantidade de peças: "))
        lavSeco = str.lower(input("Lavagem a seco?: "))
        if lavSeco == "sim":
            valor = (quantPecas * peca) + seco
            quantSeco += 1
        else:
            valor = quantPecas * peca
        totalArrecadado += valor
        print(f"O Valor do {cont} pedido foi : R${valor:.2f}")
    else:
        quantQuilo = int(input("Escreva a quantidade de quilos: "))
        lavSeco = str.lower(input("Lavagem a seco?: "))
        if lavSeco == "sim":
            valor = (quantQuilo * quilo) + seco
            quantSeco += 1
        else:
            valor = (quantQuilo * quilo)
        totalArrecadado += valor
        print(f"O Valor do {cont} pedido foi : R${valor:.2f}")
print()
print(f"Total arrecadado: R$ {totalArrecadado:.2f}")
print(f"Quantidade de lavagens a seco: {quantSeco}")