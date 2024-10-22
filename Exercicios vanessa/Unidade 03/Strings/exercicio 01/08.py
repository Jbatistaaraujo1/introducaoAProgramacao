string = str.lower(input("Escreva uma palavra ou frase: "))
novaString = ""
for i in range(len(string)):
    novaString += string[len(string) - (i + 1)]
if string == novaString:
    print("É um palidromo")
else:
    print("Não é um palidromo")