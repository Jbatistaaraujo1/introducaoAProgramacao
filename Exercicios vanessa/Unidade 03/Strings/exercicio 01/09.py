clientes = 2
listaClientes = []
for i in range(clientes):
    nome = str.lower(input("Escreva o nome do cliente: "))
    sobrenome = str.lower(input("Escreva o sobrenome do cliente: "))
    bairro = str.lower(input("Escreva o bairro do cliente: "))
    listaClientes.append([nome, sobrenome, bairro])
