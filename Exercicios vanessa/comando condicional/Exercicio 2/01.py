presente = str(input("Escreva qual foi o tipo de presente: "))
material = str(input("Escreva qual foi o material do presente "))
couro = 150
metal = 215
tecido = 100
couroBol =180

if (presente == "Relógio"):
    if(material == "Couro"):
        print(f"O valor do presente foi de: R$ {couro:.2f} e ele recebeu um chaveiro")
    elif(material == "Metal"):
        print(f"O valor do presente foi de: R$ {metal:.2f} e ele recebeu um chaveiro")
elif(presente == "Bolsa"):
    if(material == "Tecido"):
        print(f"O valor do presente foi de: R$ {tecido:.2f}")
    elif(material == "Couro"):
        print(f"O valor do presente foi de: R$ {couroBol:.2f}")