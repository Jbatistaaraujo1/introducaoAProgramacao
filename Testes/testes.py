def calcular_total_rodizio(num_pessoas, preco_rodizio):
    # Calcula quantas pessoas terão rodízio gratuito
    rodizios_gratis = num_pessoas // 10
    
    # Calcula quantas pessoas pagarão pelo rodízio
    rodizios_pagos = num_pessoas - rodizios_gratis
    
    # Calcula o total a ser pago
    total_a_pagar = rodizios_pagos * preco_rodizio
    
    # Exibe o total com duas casas decimais
    print(f"Total a ser pago: R$ {total_a_pagar:.2f}")

# Exemplo de uso
num_pessoas = int(input("Digite a quantidade de pessoas convidadas: "))
preco_rodizio = float(input("Digite o preço do rodízio: "))

calcular_total_rodizio(num_pessoas, preco_rodizio)
