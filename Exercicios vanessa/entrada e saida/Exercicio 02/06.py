pessoas = int(input("Quantidade de pessoas: "))

totalGramas = pessoas * 400
totalLatas = pessoas * 6 
precograma = 41 / 1000
precolata = 5.20

totalcerveja = totalLatas * precolata
totalcarne = totalGramas * precograma

print(f"Total cerveja: {totalcerveja:.2f}")
print(f"Total carnes: {totalcarne:.2f}")