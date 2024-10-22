def contaInicioVogal(lista):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    quantIniciaVogal = 0
    for i in range(len(lista)):
        if lista[i][0].lower() in vogal:
            quantIniciaVogal += 1
    return quantIniciaVogal
nomes = ["Eilson", "Anderson", "Luis", "Olavio", "Marco", "Sabrina"]
print(contaInicioVogal(nomes))
