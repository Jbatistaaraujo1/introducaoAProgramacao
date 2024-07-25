pessoa1 = int(input("1° pessoa:Escreva 0 ou 1 "))
pessoa2 = int(input("2° pessoa:Escreva 0 ou 1 "))
pessoa3 = int(input("3° pessoa:Escreva 0 ou 1 "))

if (pessoa1 != pessoa2) and (pessoa1 != pessoa3):
    print("1° pessoa ganhou")
elif (pessoa2 != pessoa1) and (pessoa2 != pessoa3):
    print("2° pessoa ganhou")
elif(pessoa3 != pessoa1) and (pessoa3 != pessoa2):
    print("3° pessoa ganhou")
else:
    print("Empate")