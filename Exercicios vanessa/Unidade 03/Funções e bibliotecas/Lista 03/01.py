import bibGaleriaArte

obras = []
for i in range(60):
    nomes = str.lower(input("Digite o nome da obra: "))
    obras.append(nomes)

valorTotal = 0
for i in range(len(obras)):
    if bibGaleriaArte.consultaArtista(obras[i]).lower() == "leonardo resende":
        valorTotal += bibGaleriaArte.consultaPreco(obras[i])

if valorTotal == 0:
    print("Não há Obras desse artista")
else:
    print(f"O valor total das obras de Leonardo Resende foi: R$ {valorTotal}")