# Consutas
Convenio = 170
particular = 310
# Entradas
consuConv = int(input("Quantas consultas por convênio foram feitas? "))
consuPart = int(input("Quantas consultas particulares foram feitas? "))
#Processamento 
salario = (consuConv*Convenio) + (consuPart*particular)
#Saida
print(f"O salário do médico no mês foi de:R$ {salario:.2f}")
