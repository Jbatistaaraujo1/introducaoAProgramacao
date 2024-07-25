pessoa1 = str.lower(input("1° pessoa : Escreva Pedra ou Papel ou Tesoura "))
pessoa2 = str.lower(input("2° pessoa : Escreva Pedra ou Papel ou Tesoura "))


if pessoa1 == pessoa2:
    print("Empate")
elif pessoa1 == "pedra":
    if pessoa2 == "papel":
        print(pessoa1)
    elif pessoa2 == "tesoura":
        print(pessoa1)
elif pessoa1 == "papel":
    if pessoa2 == "pedra":
        print(pessoa2)
    elif pessoa2 == "tesoura":
        print(pessoa2)
elif pessoa1 == "tesoura":
    if pessoa2 == "pedra":
        print(pessoa2)
    elif pessoa2 == "papel":
        print(pessoa1)
elif pessoa2 == "pedra":
    if pessoa1 == "papel":
        print(pessoa2)
    elif pessoa1 == "tesoura":
        print(pessoa2)
elif pessoa2 == "papel":
    if pessoa1 == "pedra":
        print(pessoa1)
    elif pessoa1 == "tesoura":
        print(pessoa1)
elif pessoa2 == "tesoura":
    if pessoa1 == "pedra":
        print(pessoa1)
    elif pessoa1 == "papel":
        print(pessoa2)