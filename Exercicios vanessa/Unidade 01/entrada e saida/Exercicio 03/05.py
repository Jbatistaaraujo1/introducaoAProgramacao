valorjogo = 39.90
bonus_por_jogo = 2.50

quantJogo = int(input("Quantidade de jogos vendidos: "))


total = valorjogo * quantJogo
salario = (total * 15 / 100)
bonustotal = bonus_por_jogo * quantJogo
pagamento = bonustotal + salario

print(f"Total arrecadado: {total:.2f}")
print(f"Bonus total: {bonustotal:.2f}")
print(f"Pagamento Total: {pagamento}")