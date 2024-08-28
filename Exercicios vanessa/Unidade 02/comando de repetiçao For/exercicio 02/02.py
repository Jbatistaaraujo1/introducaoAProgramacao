votosMarcilio = 0
votosAurelio = 0
votosBranco = 0
for cont in range(1,5,1):
    voto = str.lower(input("Escreva o seu voto: "))
    if voto == "marcílio":
        votosMarcilio += 1
    elif voto == "aurélio":
        votosAurelio += 1
    elif voto == "branco":
        votosBranco += 1
if 