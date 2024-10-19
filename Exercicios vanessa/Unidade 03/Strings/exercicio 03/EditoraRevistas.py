#a)
def PesquisaRevista(lista,nomerevista):
    for i in range(len(lista)):
        if lista[i][0].lower() == nomerevista.lower():
            return lista[i]
    return []
#b)
def PesquisaRevistasTema(lista, tema):
    listaTema = []
    for i in range(len(lista)):
        if lista[i][1].lower() == tema.lower():
            listaTema.append([lista[i][0]])
    return listaTema
#c)
def PesquisaRevistasTitulo(lista, letra):
    listaLetras = []
    for i in range(len(lista)):
        if lista[i][0][0].lower() == letra.lower():
            listaLetras.append(lista[i])
    return listaLetras
#d)
def PesquisaRevistasPreco(lista, valor):
    listaValor = []
    for i in range(len(lista)):
        if lista[i][3] <= valor:
            listaValor.append([lista[i][0],lista[i][1]])
    return listaValor
#e)
def CalculaTotalExemplares(lista, nome):
    for i in range(len(lista)):
        if lista[i][0].lower() == nome.lower():
            return lista[i][2] * 12
#f)
def CalculaPrecoMedio(lista, nome):
    for i in range(len(lista)):
        if lista[i][0].lower() == nome.lower():
            media = lista[i][3] / 12
    return media