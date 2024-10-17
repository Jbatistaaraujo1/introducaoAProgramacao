string = str.lower(input("Escreva uma string "))
vogais = ["a","e","i","o","u"]
quantVogais = 0
for i in range(len(string)):
    if string[i] in vogais:
        quantVogais += 1
print(quantVogais)