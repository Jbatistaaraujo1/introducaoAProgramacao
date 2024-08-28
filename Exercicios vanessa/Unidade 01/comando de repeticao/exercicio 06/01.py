sair = "não"
quantHabPequena = 0
quantHabMedia = 0
quantHabGrande = 0
contMedia = 0
contGrande = 0
while (sair !="sim"):
    quantHabitantes = int(input("Escreva a quantidade de habitantes: "))
    if (quantHabitantes > 0) and (quantHabitantes <= 5000):
        print("Cidade Pequena")
        quantHabPequena += quantHabitantes
    elif(quantHabitantes > 5000) and (quantHabitantes <= 10000):
        print("Cidade Média")
        quantHabMedia += quantHabitantes
        contMedia += 1
    elif(quantHabitantes > 10000):
        print("Cidade Grande")
        quantHabGrande += quantHabitantes
        contGrande += 1
    else:
        print("Quantidade de habitantes inválida")
    quantTotal = quantHabGrande + quantHabPequena + quantHabMedia
    sair = str.lower(input("Deseja sair? "))
print(quantHabPequena)
print(contMedia)
if quantHabGrande > 0:
    media = quantHabGrande // contGrande
else:   
    media = 0 
print(media)
print(quantTotal)