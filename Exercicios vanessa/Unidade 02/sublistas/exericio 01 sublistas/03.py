Estados = []
quantEstados = 10
for i in range(quantEstados):
    nome = str.lower(input("Escreva o nome do Estado: "))
    regiao = str.lower(input("Escreva a Região: "))
    quantMunicipios = int(input("Escreva a quantidade de Munícipios: "))
    quantHabitantes = int(input("Escreva a quantidade de Habitantes: "))
    Estados.append([nome,regiao,quantMunicipios,quantHabitantes])
# O nome de todos os Estados da Região Sul
nomeSul = []
for i in range(quantEstados):
    if Estados[i][1] == "sul":
        nomeSul.append(Estados[i][0])  
print(f"O nome de todos os Estados da Região Sul: {nomeSul}")    
# A quantidade de Estados da Região Nordeste com mais de 100 municípios
quantNordesteMais100 = 0
for i in range(quantEstados):
    if Estados[i][1] == "nordeste":
        if Estados[i][2] > 100:
            quantNordesteMais100 += 1
print(f"A quantidade de Estados da Região Nordeste com mais de 100 municípios foi: {quantNordesteMais100}")
# A quantidade total de cidades dos Estados da Região Norte
totalCidadesNorte = 0
for i in range(quantEstados):
    if Estados[i][1] == "norte":
        totalCidadesNorte += Estados[i][2]
print(f"A quantidade total de cidades dos Estados da Região Norte foi: {totalCidadesNorte}")
# A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes
quantEstadosCentro = 0
for i in range(quantEstados):
    if Estados[i][1] == "centro-oeste":
        if Estados[i][3] < 500000:
            quantEstadosCentro += 1
print(f"A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes: {quantEstadosCentro}")
# A quantidade média de habitantes dos Estados da Região Sudeste
totalHabitantesSudeste = 0 
quantEstadosSudeste = 0
for i in range(quantEstados):
    if Estados[i][1] == "sudeste":
        totalHabitantesSudeste += Estados[i][3]
        quantEstadosSudeste += 1
mediaHabitantesSudeste = totalHabitantesSudeste / quantEstadosSudeste
print(f"A quantidade média de habitantes dos Estados da Região Sudeste: {mediaHabitantesSudeste}")
