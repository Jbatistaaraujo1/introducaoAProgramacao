quantPortugues = int(input("Quantidade de questoes de portugues: "))

quantAprovados = 0
while quantPortugues > 0:
    quantMat = int(input("Quantidade de questoes de matematica: "))
    quantRed = float(input("Nota da redação: "))
    if quantPortugues >= 40 and quantMat >= 21 and quantRed >= 7:
        quantAprovados += 1
    quantPortugues = int(input("Quantidade de questoes de portugues: "))
print(f"A quantidade de aprovados foi {quantAprovados}")