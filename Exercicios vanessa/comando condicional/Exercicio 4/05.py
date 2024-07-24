tempoServico = int(input("Escreva o tempo de serviço: "))
salarioAtual = float(input("Escreva o salário atual: "))

if tempoServico >= 55:
    valor = (salarioAtual * 60 / 100) + ((tempoServico - 55)* (salarioAtual *15 / 100))
    print(f"O banefício é de R$ {valor:.2f}")
else:
    print("Não tem direito ao benefício")
