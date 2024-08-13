tipoPassagem = str.lower(input("Escreva o tipo de passagem: "))
estudante = 4.50
inteira = 9.00
idoso = 3.00
quantEstudante = 0
quantIdoso = 0
while tipoPassagem != "fim":
    if tipoPassagem == "estudante":
        quantEstudante += 1
    elif tipoPassagem == "idoso":
        quantIdoso += 3
    tipoPassagem = str.lower(input("Escreva o tipo de passagem: "))
print(f"A quantidade de estudantes foi de {quantEstudante}")
print(f"O valor total de passagens de idosos foi de R$ {quantIdoso:.2f}")
