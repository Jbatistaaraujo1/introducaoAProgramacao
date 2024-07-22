quantConvi = int(input("Quantidade de convidados: "))
precoRodz = int(input("Preço do Rodízio: "))
rodgrat = quantConvi // 10

if (quantConvi >= 10):
    valortotal = (quantConvi - rodgrat) * precoRodz 
else:
    valortotal = quantConvi * precoRodz
    
print(f"Total a pagar: {valortotal:.2f}")