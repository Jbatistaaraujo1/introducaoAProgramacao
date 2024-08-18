nome = input()
salario_fixo = float(input())
vendas = float(input())

comissao = vendas * 15/100
salario_total = comissao + salario_fixo

print(f"TOTAL = R$ {salario_total:.2f}")