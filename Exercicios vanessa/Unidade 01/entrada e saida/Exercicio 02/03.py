quantBri = int(input("Quantidade de brigadeiros: "))
quantBei = int(input("Quantidade de beijinhos: "))
quantCri = int(input("Quantidade de crianças convidadas: "))

brigadeiro = 1.90
beijinho = 1.70

valortotal = (quantBri*brigadeiro) + (quantBei*beijinho)
totaldoc = quantBei+quantBri
totalcri = totaldoc // quantCri

print(f"Valor total gasto é: R$ {valortotal:.2f}")
print(f"Quantidade de docinhos por criança: {totalcri}")
