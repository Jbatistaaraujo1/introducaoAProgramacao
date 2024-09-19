animais = []
quantAnimais = 100

for i in range(quantAnimais):
    nome = str.lower(input("Escreva o nome do animal: "))
    idade = float(input("Escreva a idade do animal: "))
    tipo = str.lower(input("Escreva o tipo: "))
    animais.append([nome,idade,tipo])
# A quantidade de cachorros cadastrados
quantCachorros = 0
for i in range(quantAnimais):
    if animais[i][2] == "cachorro":
        quantCachorros += 1
print()
print(f"A quantidade de cachorros cadastrados: {quantCachorros}")
# O nome de todos os gatos
nomeGatos = []
for i in range(quantAnimais):
    if animais[i][2] == "gato":
        nomeGatos.append(animais[i][0])
print()
print(f"O nome de todos os gatos: {nomeGatos}")
# As idades dos pássaros
idadesPassaros = []
for i in range(quantAnimais):
    if animais[i][2] == "pássaros":
        idadesPassaros.append(animais[i][1])
print()
print(f"As idades dos pássaros: {idadesPassaros}")
# Os nomes dos animais com menos de um ano
nomesMenor1Ano = []
for i in range(quantAnimais):
    if animais[i][1] < 1:
        nomesMenor1Ano.append(animais[i][0])
print()
print(f"Os nomes dos animais com menos de um ano: {nomesMenor1Ano}")
# A média de idade dos gatos
quantGatos = 0
totalIdadeGatos = 0
for i in range(quantAnimais):
    if animais[i][2] == "gato":
        quantGatos += 1
        totalIdadeGatos += animais[i][1]
mediaIdadeGatos = totalIdadeGatos / quantGatos
print()
print(f"A média de idade dos gatos: {mediaIdadeGatos}")