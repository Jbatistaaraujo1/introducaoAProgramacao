quantAno = 0
valorTotal = 0
valorAntigo = 0
for cont in range(1,1501):
    descricao = str.lower(input("Escreva a descrição do item: "))
    valor = int(input("Escreva o valor do item: "))
    ano = int(input("Escreva o ano do item: "))
    if ano < 1827:
        quantAno += 1
    if valor > valorAntigo:
        descricaoMaior = descricao
        anoMaior = ano
    valorTotal += valor
    valorAntigo = valor
if cont > 1:    
    valorMedio = valorTotal / cont
else:
    valorMedio = valorTotal
print(f"Itens produzidos antes de 1827 = {quantAno}")
print(f"Valor médio dos itens = {valorMedio:.2f}")
print(f"Dados do objeto mais valioso = {descricaoMaior},{anoMaior}")
