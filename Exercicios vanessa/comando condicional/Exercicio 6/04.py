valorProduto = int(input("Valor do produto: "))
quantAnos = int(input("Quantidade de anos de garantia: "))

if quantAnos == 0:
    print(f"O valor total foi de R$ {valorProduto:.2f}")
elif quantAnos == 1:
    valor = valorProduto + (valorProduto * 3 / 100)
    print(f"O valor total foi de R$ {valor:.2f}")
elif quantAnos == 2:
    valor = valorProduto + (valorProduto * 5 / 100)
    print(f"O valor total foi de R$ {valor:.2f}")
    
