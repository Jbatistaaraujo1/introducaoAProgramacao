def MediaInteiraLista(lista):
    somaLista = 0
    for i in range(len(lista)):
        somaLista += lista[i]
    media = somaLista // len(lista)
    if len(lista) == 0:
        return 0
    else:
        return media
    

def multiplicaLista(lista, valor):
    if (len(lista) == 0):
        return []
    else:
        novaLista = []
        for i in range(len(lista)):
            novaLista.append(lista[i] * valor)
        return novaLista


