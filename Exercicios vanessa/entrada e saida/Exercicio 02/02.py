valorIpva = float(input("Valor do Ipva(sem desconto) do veiculo: "))
valorTaxa = float(input("Valor da taxa de transito do veiculo: "))

desconto = valorIpva - (valorIpva * 5/100)
total = desconto + valorTaxa

print(f"O valor a ser pago é de: R${total}")