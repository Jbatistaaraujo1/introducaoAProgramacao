atletas = [["Simone Biles", "Feminino", "EUA", "Ginástica", 26],
["Usain Bolt", "Masculino", "Jamaica", "Atletismo", 37],
["Naomi Osaka", "Feminino", "Japão", "Tênis", 26],
["Lionel Messi", "Masculino", "Argentina", "Futebol", 37],
["Serena Williams", "Feminino", "EUA", "Tênis", 42],
["Gabriel Medina", "Masculino", "Brasil", "Surfe", 30],
["Marta Silva", "Feminino", "Brasil", "Futebol", 38],
["Michael Phelps", "Masculino", "EUA", "Natação", 39],
["Katie Ledecky", "Feminino", "EUA", "Natação", 27],
["Novak Djokovic", "Masculino", "Sérvia", "Tênis", 37],
["Rafaela Silva", "Feminino", "Brasil", "Judô", 31],
["LeBron James", "Masculino", "EUA", "Basquete", 39]]


# a) Calcular e exibir a média de idade de todos os atletas
totalIdadeAtletas = 0
for i in range(len(atletas)):
    totalIdadeAtletas += atletas[i][4]
mediaIdadeAtletas = totalIdadeAtletas // i
print(f"A média de idade de todos os atletas: {mediaIdadeAtletas}")
print()

# b) Exibir o nome e a idade do atleta mais velho
maiorIdade = 0
for i in range(len(atletas)):
    if atletas[i][4] > maiorIdade :
        maiorIdade = atletas[i][4]
        nomeMaiorIdade = atletas[i][0]
print(f"O nome e a idade do atleta mais velho: {nomeMaiorIdade},{maiorIdade} anos.")
print()

# c) Criar e exibir uma lista, com sublistas, contendo o nome e o esporte de cada atleta brasileiro.
nomeEsporte = []
for i in range(len(atletas)):
    nomeEsporte.append([atletas[i][0],atletas[i][3]])
print(f"Criar e exibir uma lista, com sublistas, contendo o nome e o esporte de cada atleta brasileiro: {nomeEsporte}")
print()

# d) Calcular e exibir quantos atletas são do gênero feminino.
quantFeminino = 0
for i in range(len(atletas)):
    if atletas[i][1].lower() == "feminino":
        quantFeminino += 1
print(f"Calcular e exibir quantos atletas são do gênero feminino: {quantFeminino}")
print()
# e) Exibir o nome e o esporte dos atletas com menos de 30 anos.
for i in range(len(atletas)):
    if atletas[i][4] < 30:
        print(atletas[i][0],atletas[i][3])
print()
# f) Exibir o nome dos atletas cujo esporte seja tênis.
for i in range(len(atletas)):
    if atletas[i][3].lower() == "tênis":
        print(atletas[i][0])
print()

# g) Exibir a idade do atleta do gênero masculino mais novo.
idadeMaisNovo = 0
for i in range(len(atletas)):
    if atletas[i][1].lower() == "masculino":
        if idadeMaisNovo == 0:
            idadeMaisNovo = atletas[i][4]
        else:
            if atletas[i][4] < idadeMaisNovo:
                idadeMaisNovo = atletas[i][4]
print(idadeMaisNovo)
print()

# h) Exibir os nomes dos atletas que não são dos EUA.
for i in range(len(atletas)):
    if atletas[i][2].lower() != "eua":
        print(atletas[i][0])
print()

# i) Criar e exibir uma lista, com sublistas, contendo os nomes e idades dos atletas que praticam futebol.
futebol = []
for i in range(len(atletas)):
    if atletas[i][3].lower() == "futebol":
        futebol.append([atletas[i][0],atletas[i][4]])
print(futebol)

# j) Receber como entrada o nome de um país, e exibir os nomes de todos os atletas desse país. Caso o país não tenha atletas na lista, exiba uma mensagem informando.
pais = str.lower(input("Escreva o nome do País: "))
quantPais = 0
pais = []
for i in range(len(atletas)):
    if atletas[i][2].lower() == pais:
        quantPais += 1
        nomeatleta = atletas[i][2]
        pais.append(nomeatleta)
if quantPais >= 1:
    print(pais)
else:
    print("Não tem nenhum País.")
print()

# k) Calcular e exibir a diferença de idade entre o atleta mais velho e o mais novo
idadeMaisVelho = 0
idadeMaisNovo =0
menorIdade = 0
for i in range(len(atletas)):
    if atletas[i][4] > idadeMaisVelho:
        idadeMaisVelho = atletas[i][4]
    if menorIdade == 0:
        menorIdade += 1
        idadeMaisNovo = atletas[i][4]
    else:
        if atletas[i][4] < idadeMaisNovo:
            idadeMaisNovo = atletas[i][4]
diferencaIdade = idadeMaisVelho - idadeMaisNovo
print(diferencaIdade)
print()

#l) Receber como entrada um gênero e exibir a média de idade dos atletas desse gênero. Caso não haja atletas do gênero informado, exiba uma mensagem.
genero = str.lower(input("Escreva o genero: "))
quantGenero = 0
totalIdadeGenero = 0
for i in range(len(atletas)):
    if atletas[i][1].lower() == genero:
        totalIdadeGenero += atletas[i][4]
        quantGenero += 1
mediaGenero = totalIdadeGenero // quantGenero
if quantGenero >= 1:
    print(mediaGenero)
else:
    print("Gênero Não está na lista")

# m) Calcular e exibir quantos atletas têm idade entre 25 e 35 anos, e qual é a porcentagem deles em relação ao total de atletas
quantAtletasIdadeEntre25e35 = 0
for i in range(len(atletas)):
    if atletas[i][4] >= 25 and atletas[i][4] <= 35:
        quantAtletasIdadeEntre25e35 += 1
percentual = (quantAtletasIdadeEntre25e35 / len(atletas)) * 100
print(f"{percentual:.2f}%")

# n) Exibir, sem repetição, os esportes dos atletas que têm mais de 30 anos.
maioresDe30 = []
for i in range(len(atletas)):
    if atletas[i][4] > 30:
        if atletas[i][3] not in maioresDe30:
            maioresDe30.append(atletas[i][3])
print(maioresDe30)