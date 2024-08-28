quantFeijoada = 0
quantChurrasco = 0
cont = 0
while (cont < 20):
    escolha = str.lower (input ("Sua escolha: "))
    if (escolha == "churrasco"):
        quantChurrasco = quantChurrasco + 1
    else:
        quantFeijoada = quantFeijoada + 1
    cont = cont + 1
if (quantChurrasco > quantFeijoada):
    print("Churrasco foi o mais votado")
elif(quantFeijoada>quantChurrasco):
    print("Feijoada foi a mais votada")
else:
    print("Empate")
    