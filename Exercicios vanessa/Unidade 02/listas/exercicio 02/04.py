provas = 5
listaLcc = []
listaBsi = []

for cont in range(provas):
    pontoLcc = int(input("Escreva a quantidade de pontos de Lcc: "))
    listaLcc.append(pontoLcc)
print()
for cont in range(provas):
    pontoBsi = int(input("Escreva a quantidade de pontos de Si: "))
    listaBsi.append(pontoBsi)
quantVitoriasLcc = 0
quantVitoriasBsi = 0
quantEmpates = 0
for i in range(provas):
    if listaLcc[i] > listaBsi[i]:
        quantVitoriasLcc += 1
    if listaBsi[i] > listaLcc[i]:
        quantVitoriasBsi += 1
    if listaLcc[i] == listaBsi[i]:
        quantEmpates += 1
print(f"Vitórias LCC: {quantVitoriasLcc}")
print(f"Vitórias BSI: {quantVitoriasBsi}")
print(f"Empates: {quantEmpates}")
if quantVitoriasBsi > quantVitoriasLcc:
    print("BSI")
elif quantVitoriasLcc > quantVitoriasBsi:
    print("LCC")
else:
    print("EMPATE")