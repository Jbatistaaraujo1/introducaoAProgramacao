quantVeiculos = int(input("Escreva a quantidade de veiculos: "))
total_Arrecadado = 0
casa = 0
while quantVeiculos != 555:
    if quantVeiculos >2:
       multa = (quantVeiculos - 2) * 10
       casa += 1       
       print(f"Multa casa: R$ {multa}")
       total_Arrecadado += multa
    elif(quantVeiculos >0 and quantVeiculos <= 2):
        multa = 0
        casa += 1
        print(f"Multa casa: R$ {multa}")
    quantVeiculos = int(input("Escreva a quantidade de veiculos: "))
print(f"Total arrecadado: R$ {total_Arrecadado}")
