listaNome = []
listaEstado = []
listaPontos = []
quantTimes = int(input("Escreva a quantidade de times que estão participando: "))

for cont in range(quantTimes):
    nome = str.lower(input("Escreva o nome do time: "))
    estado = str.lower(input("Escreva o estado do time: "))
    pontos = int(input("Escreva a quantidade de pontos: "))
    listaNome.append(nome)
    listaEstado.append(estado)
    listaPontos.append(pontos)
listaAcima100 = []
for i in range(quantTimes):
    if listaEstado[i] == "pb" or listaEstado[i] == "pe":
        if pontos[i] > 100:
            listaAcima100.append(listaNome[i])
print(f"Os nomes de todos os times de PB e PE com mais de 100 pontos: {listaAcima100}")

for i in range(quantTimes):
    nomeInf = str.lower(input("Digite o nome do time que você deseja saber a pontuação: "))
    if listaNome[i] == nomeInf:
        print(f"A quantidade de pontos de um time informado pelo usuário: {listaNome[i]}") 
listaPontosMg = []
for i in range(quantTimes):
    if listaEstado[i] == "mg":
        listaPontosMg.append(listaPontos[i])
        print(f"A lista de pontuações dos times de MG: {listaPontosMg}")
totalpontos = 0
cont = 0
for i in range(quantTimes):
    if listaEstado[i] == "rj":
        totalpontos += listaPontos[i]
        cont += 1
media = totalpontos / cont
print(f"A média de pontos dos times do RJ: {media}")
maiorPontuacao = listaPontos[0]
for i in range(quantTimes):
    if listaPontos[i] > maiorPontuacao:
        maiorPontuacao = listaPontos[i]
        nomeMaior = listaNome[i]
print(f"O nome do time que teve a maior pontuação: {nomeMaior}")

