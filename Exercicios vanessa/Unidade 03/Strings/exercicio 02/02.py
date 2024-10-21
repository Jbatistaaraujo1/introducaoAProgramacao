def contaPalavras(frase):
    espaco = " "
    quantEspaco = 0
    for i in range(len(frase)):
        if frase[i] == espaco:
            quantEspaco += 1
    return quantEspaco + 1

print(contaPalavras("Joao Batista De Araujo"))