letras = str.lower(input("Escreva uma letra: "))
quantEspeciais = 0

while (letras != "x"):
    if letras == "k" or letras == "y" or letras == "w":
        quantEspeciais += 1
    letras = str.lower(input("Escreva outra letra: "))

print(f"As letras especiais foram digitadas {quantEspeciais} vezes!")