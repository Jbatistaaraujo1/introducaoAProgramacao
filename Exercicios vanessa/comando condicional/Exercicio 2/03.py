tipoDeCombustivel = str(input("Qual o tipo de combustível? "))
valorDinheiro = int(input("Qual o valor que deseja gastar? "))
gasolina = 2.53
etanol = 2.09
diesel = 1.92
if (tipoDeCombustivel == "Gasolina"):
    litros = valorDinheiro / gasolina
    print(f"Litros: {litros:.2f} e não ganhou troca de óleo")
elif(tipoDeCombustivel == "Etanol"):
    litros = valorDinheiro / etanol
    if(litros > 30):
        print(f"Litros: {litros:.2f} e ganhou troca de óleo")
    else:
        print(f"Litros: {litros:.2f} e não ganhou troca de óleo")
elif(tipoDeCombustivel == "Diesel"):
    litros = valorDinheiro / diesel 
    print(f"Litros: {litros:.2f} e não ganhou troca de óleo")
