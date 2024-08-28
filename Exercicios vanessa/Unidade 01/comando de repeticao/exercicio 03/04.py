continuar = "sim"
valorPessoa = 14
quantPessoas = 0
custoFesta = 0
while (continuar != "não") and (continuar != "nao"):
    quantConvidados = int(input("Digite a quantidade de convidados: "))
    quantPessoas = quantConvidados + quantPessoas +1
    custoFesta = (quantConvidados * valorPessoa) + custoFesta + valorPessoa
    continuar = str.lower(input("Deseja continuar? Digite sim ou não: "))
print(f"O custo da festa foi de R$ {custoFesta}")
print(f"O total de participante foi de {quantPessoas}")