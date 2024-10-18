string = str.lower(input("Escreva uma string: "))
letra = str.lower(input("Escreva uma letra a ser buscada: "))


if letra in string:
    print("Está Presente")
else:
    print("Não Está Presente")