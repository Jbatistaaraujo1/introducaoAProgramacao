def contaMaisDe3(lista):
    vogal = ["a","e","i","o","u"]
    quantPalavras = 0
    for i in range(len(lista)):
        quantVogal = 0
        palavra = lista[i]
        for i in range(len(palavra)):
            if palavra[i].lower() in vogal:
                quantVogal += 1
        if quantVogal > 3:
            quantPalavras += 1
    return quantPalavras



lista_palavra = ['Planaltoa', 'Agua Fria', 'Cenaatro', 'Bnacaeurs', 'mtsranmaei']
print(contaMaisDe3(lista_palavra))