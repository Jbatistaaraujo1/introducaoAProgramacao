qtde = 0
notaAnterior = 0
for cont in range(1,7,1):
    nota = float(input("Escreva a nota:"))
    if nota > notaAnterior :
        melhorNota = nota
        qtde += 1
    notaAnterior = nota
if qtde == 6:
    print("Ganha Brinquedo!")
else:
    print("Não Ganha Brinquedo!")