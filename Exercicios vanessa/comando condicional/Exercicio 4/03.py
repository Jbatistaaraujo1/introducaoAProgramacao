setor = str(input("Qual o setor? "))
ingresso = str(input("Qual o tipo de ingresso? "))

vip = 350
cadeira = 200
arquibancada = 100
meia = 50/100
taxa = 5/100 
if (setor=="Arquibancada"):
    if ingresso == "Inteira":
        valor = (taxa * arquibancada) + arquibancada 
        print(f"{valor:.2f}")
    elif (ingresso == "Meia"):
        valor = (taxa * arquibancada) + (arquibancada * meia)
        print(f"{valor:.2f}")
    else:
        print("Tipo de ingresso inválido")
elif(setor == "Cadeira"):
    if ingresso == "Inteira":
        valor = (taxa * cadeira) + cadeira
        print(f"{valor:.2f}")
    elif (ingresso == "Meia"):
        valor = (taxa * cadeira) + (cadeira * meia)
        print(f"{valor:.2f}")
    else:
        print("Tipo de ingresso inválido")
elif(setor == "Platéia VIP"):
    if ingresso == "Inteira":
        valor = (taxa * vip) + vip
        print(f"{valor:.2f}")
    else:
         print("Tipo de ingresso inválido")
else:
    print("Setor inválido")