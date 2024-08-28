votoMarcilio = 0
votoAurelio = 0
votoBranco = 0
for cont in range(1,5,1):
    voto = str.lower(input("Escreva o nome do candidato: "))
    if (voto == "marcílio" ):
        votoMarcilio += 1
    elif(voto == "aurelio"):
        votoAurelio += 1
    else:
        votoBranco += 1
if votoMarcilio > votoAurelio and votoMarcilio > votoBranco:
    print("Marcílio")
elif votoAurelio > votoMarcilio and votoAurelio > votoBranco:
    print("Aurélio")
elif votoBranco >= votoMarcilio and votoBranco >= votoAurelio:
    print("Nova votação")
else:
    print("Nova votação")
############