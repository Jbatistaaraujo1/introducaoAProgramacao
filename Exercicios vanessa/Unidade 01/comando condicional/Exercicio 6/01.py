tipo1 = str.lower(input("Qual o tipo? "))
tipo2 = str.lower(input("Qual o tipo? "))

#Ternos:
simples = 120.40 - (120.40 * 7 / 100)
completo = 150.35 - (150.35 * 7 /100)
fraque = 180.70 - (180.70 * 7 / 100)
#Acessórios:
gravata = 30
sapato = 80
cinto = 15

if tipo1 == "acessório":
    if tipo2 == "gravata":
        print(f"O valor total foi de R$ {gravata:.2f}")
    elif tipo2 == "sapato":
        print(f"O valor total foi de R$ {sapato:.2f}")
    elif tipo2 == "cinto":
        print(f"O valor total foi de R$ {cinto:.2f}")
    else:
        print("Acessório invalido")
elif tipo1 == "terno":
    if tipo2 == "simples":
        print(f"O valor total foi de R$ {simples:.2f}")
    elif tipo2 == "completo":
        print(f"O valor total foi de R$ {completo:.2f}")
    elif tipo2 == "fraque":
        print(f"O valor total foi de R$ {fraque:.2f}")
    else:
        print("Tipo de terno inexistente")
else:
    print("Inexistente")