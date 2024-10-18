texto = str(input("Escreva um texto: "))
letra = ["K","W","Y","k","w","y"]
novoTexto = ""
for i in range(len(texto)):
    if texto[i] not in letra:
        novoTexto += texto[i]
print(novoTexto)