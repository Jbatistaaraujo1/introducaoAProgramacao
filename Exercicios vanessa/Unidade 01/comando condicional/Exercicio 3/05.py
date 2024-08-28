filme = str(input("Qual o modo do filme? "))
lanche = str(input("Qual o lanche? "))

filme2d = 8.50
filme3d = 14.50
comboSimples = 10
comboCompleto = 12

if(filme == "2D"):
    if(lanche == "Combo simples"):
        valor = filme2d + comboSimples
        print(f"Valor:R${valor:.2f}")
    elif(lanche == "Combo completo"):
        valor = filme2d + comboCompleto
        print(f"Valor:R${valor:.2f}")
    else:
        valor = filme2d
        print(f"Valor:R${valor:.2f}")
elif(filme == "3D"):
    if(lanche == "Combo simples"):
        valor = filme3d + comboSimples
        print(f"Valor:R${valor:.2f}")
    elif(lanche == "Combo completo"):
        valor = filme3d + comboCompleto
        print(f"Valor:R${valor:.2f}")
    else:
        valor = filme3d
        print(f"Valor:R${valor:.2f}")