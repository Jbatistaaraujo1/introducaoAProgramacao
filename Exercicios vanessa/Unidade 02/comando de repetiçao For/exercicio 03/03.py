totalBranco = 0
totalMarfim = 0
totalBras = 0
totalEletro = 0
precoTotal = 0
quantDecoracao = 0
for cont in range (1):
    tipo = str.lower(input("Escreva o tipo de produto: "))
    if tipo == "móvel":
        cor = str.lower(input("Qual a cor: "))
        if cor == "branco":
            totalBranco += 1
        else:
            totalMarfim += 1
    elif tipo == "eletrodoméstico":
        marca = str.lower(input("Qual a marca: "))
        if marca == "brastemp":
            totalBras += 1
        else:
            totalEletro += 1
    else:
        descricao = str.lower(input("Escreva a descrição: "))
        preco = int(input("Escreva o preço: "))
        precoTotal += preco
        quantDecoracao += 1
print()
totalMovel = totalBranco + totalMarfim
if totalBranco >=1:
    percentualBranco = (totalMovel / totalBranco) * 100
elif totalMarfim >=1:    
    percentualMarfim = (totalMovel / totalMarfim) * 100
else:
    print("Não foi vendido nenhum móvel")  
print(f"Percentual marfim {percentualMarfim}, percentual branco {percentualBranco}")
if(totalBras >= 1) or (totalEletro >=1):
    if totalBras > totalEletro:
        print(f"Marca mais Vendida: Brastemp")
    elif totalEletro > totalBranco:
        print(f"Marca mais Vendida: Eletrolux")
    elif totalBras == totalEletro:
        print("As duas marcas foram vendidas igualmente")
else:
    print("Nenhum eletrodomestico foi vendido")

if quantDecoracao >= 1:
    precoTotal = precoTotal // quantDecoracao
    print(f"Preço médio de decoração: {precoTotal}")
else:
    print("Nenhum objeto de decoração foi vendido")
