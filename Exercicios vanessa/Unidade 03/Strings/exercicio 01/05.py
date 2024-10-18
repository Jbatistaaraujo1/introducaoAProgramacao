string = str(input("Escreva uma String: "))
novaString = ""
for i in range(len(string)):
    novaString += string[len(string) - (i + 1)]
print(novaString)