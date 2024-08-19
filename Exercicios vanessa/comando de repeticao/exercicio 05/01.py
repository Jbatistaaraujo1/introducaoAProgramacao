idade = int(input("Escreva sua idade: "))
maiorIdade = 0
jovens = 0
idoso = 0
quantIdoso = 0
while (idade >=0):
    if idade < 20:
        jovens += 1
    elif (idade >= 20) and (idade <= 60):
        if idade > maiorIdade:
            maiorIdade = idade
    else:
        idoso += idade
        quantIdoso += 1
    idade = int(input("Escreva sua idade: "))
if jovens >= 1:
    print(f"A quantidade de pessoas jovens é de {jovens}")
else:
    print("Não há jovens")
if maiorIdade >=1:
    print(f"A maior idade Adulto é de {maiorIdade}")
else:
    print("Não há adultos")
if quantIdoso >= 1 :
    media = idoso / quantIdoso
    print(f"A média  de idosos foi de {media}")
else:
    print("Não há idosos")