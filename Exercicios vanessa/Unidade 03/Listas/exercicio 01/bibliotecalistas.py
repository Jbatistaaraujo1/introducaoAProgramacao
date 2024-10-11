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

def Busca(lista, valor):
    if len(lista) == 0:
        return False
    if valor in lista:
        return True
    else:
        return False
    
def ContaOcorrencias(lista, valor):
    quantVezes = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            quantVezes += 1
    return quantVezes

def RemoveValor(lista, valor):
    novalista = []
    for i in range(len(lista)):
        if lista[i] != valor:
            novalista.append(lista[i])
    return novalista

def SemRepeticao(lista):
    novalista = []
    for i in range(len(lista)):
        if lista[i] not in novalista:
            novalista.append(lista[i])
    return novalista

def TestaOrdenacao(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
        