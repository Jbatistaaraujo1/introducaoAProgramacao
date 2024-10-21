import bibString

quantConsoantes = 0
for i in range(10):
    palavra = str.lower(input("Escreva uma palavra: "))
    quantConsoantes += len(bibString.RemoveVogais(palavra))

print(quantConsoantes)