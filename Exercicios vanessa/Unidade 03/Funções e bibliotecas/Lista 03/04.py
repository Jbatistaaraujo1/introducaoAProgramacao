import bibGaleriaArte
valorTotal = 0
quantQuadros = 0
for i in range(80):
    nome = str.lower(input("Digite o nome da obra: "))
    if bibGaleriaArte.consultaTipo(nome) == "quadros":
        valorTotal += bibGaleriaArte.consultaPreco(nome)
        quantQuadros += 1
media = valorTotal / quantQuadros
if quantQuadros >= 1:
    print(media)
else:
    print("Não há quadros")