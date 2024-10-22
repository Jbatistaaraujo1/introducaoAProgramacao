def contaTotalH(lista):
    letra = "h"
    quantH = 0
    for i in range(len(lista)):
        palavra = lista [i]
        for i in range(len(palavra)):
            if palavra[i].lower() == letra:
                quantH += 1
    return quantH


lista = ["hiato", "pato", "rinoceronte", "elefante", "hgainha", "hiena"]
print(contaTotalH(lista))