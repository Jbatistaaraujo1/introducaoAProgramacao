import bibGaleriaArte

quantQuadros = 0
quantEsculturas = 0
for i in range(50):
    nome = str.lower(input("Digite o nome da obra: "))
    if bibGaleriaArte.consultaTipo(nome).lower() == "quadros":
        quantQuadros += 1
    else:
        quantEsculturas += 1
if quantQuadros > quantEsculturas:
    print("Dispõe de uma quantidade maior de quadros")
else:
    print("Dispõe de uma quantidade maior de esculturas")
