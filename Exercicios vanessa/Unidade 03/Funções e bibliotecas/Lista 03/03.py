import bibGaleriaArte
Obras = []
for i in range(30):
    nome = str.lower(input("Digite o nome da obra: "))
    Obras.append(nome)
quantEsculturas = 0
for i in range(30):
    if bibGaleriaArte.consultaArtista(Obras[i]) == "adélia machado":
        if bibGaleriaArte.consultaTipo.lower() == "escultura":
            quantEsculturas += 1
print(quantEsculturas)