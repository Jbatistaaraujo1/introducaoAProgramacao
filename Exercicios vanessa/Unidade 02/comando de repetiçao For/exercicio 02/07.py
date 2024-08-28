meta = 0
total = 0
for cont in range(1,8,1):
    quantCorres = int(input("Escreva a quantidade de correspondências: "))
    total += quantCorres
    if quantCorres >= 100:
        meta += 1
media = total // cont
print(f"Cumpriu a meta em {meta} dias")
print(f"Média de entregas:{media}")