string = str(input("Escreva uma String: "))
letra = "A"
novaString = ""
for i in range(len(string)):
    if letra.lower() != string[i].lower():
        novaString += string[i]
print(novaString)