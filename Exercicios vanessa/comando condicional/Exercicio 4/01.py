#Time 01
time01 = str(input("Escreva o nome do 1º time: "))
pontos1 = int(input("Escreva a quantidade de pontos: "))
saldo1 = str(input("Escreva o saldo de gols: "))
gol1 = str(input("Escreva a quantidade de gols feitos: "))
#Time 02
time02 = str(input("Escreva o nome do 2º time: "))
pontos2 = int(input("Escreva a quantidade de pontos: "))
saldo2 = str(input("Escreva o saldo de gols: "))
gol2 = str(input("Escreva a quantidade de gols feitos: "))

if (pontos1>pontos2):
    print(time01.lower())
elif (pontos2>pontos1):
    print(time02.lower())
elif(pontos1==pontos2):
    if saldo1>saldo2:
        print(time01.lower)
    elif(saldo2>saldo1):
        print(time02.lower)
    elif(saldo1==saldo2):
        if (gol1>gol2):
            print(time01.lower)
        elif(gol2>gol1):
            print(time02.lower)
        else:
            print("EMPATE")
else:
    print("EMPATE")