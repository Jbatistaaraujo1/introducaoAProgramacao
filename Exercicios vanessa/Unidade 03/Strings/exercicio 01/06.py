texto = str(input("Escreva um texto: "))
simbolos = [".",",",":",";","!","?"]
quantSimbolos = 0
for i in range(len(texto)):
    if texto[i] in simbolos:
        quantSimbolos += 1
print(quantSimbolos)
