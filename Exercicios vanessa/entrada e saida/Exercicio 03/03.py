funcionariosMulheres = int(input("Quantidade de funcionarias Mulheres: "))
funcionariosHomens = int(input("Quantidade de funcionario Homens: "))

valorpanetone = 12.50
valorvinho = 17
homens = valorpanetone * funcionariosHomens
Mulheres = valorvinho * funcionariosMulheres
Total = Mulheres + homens
valormedio = Total / (funcionariosHomens + funcionariosMulheres) 

print(f"Valor total gasto com presentes: R${Total:.2f}")
print(f"Valor medio gasto com presentes: R${valormedio:.1f}")