quantConvi = int(input("Quantidade de convidados: "))
precoRodz = int(input("Preço do Rodízio: "))

if (quantConvi >= 10):
    valortotal = (quantConvi - 1) * precoRodz 
else:
    valortotal = quantConvi * precoRodz
    
print(f"Total a pagar: {valortotal:.2f}")