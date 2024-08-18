nomeItem = str.lower(input("Titulo: "))
duracao = int(input("Duraçao da assinatura: "))

mural = 200
oCoreto = 235
meuLar = 180
suaMesa = 230

if nomeItem == "mural":
    valor = (mural * duracao)
    print(f"O valor total foi de R$ {valor:.2f}")
elif nomeItem == "o coreto":
    valor = (oCoreto * duracao)
    print(f"O valor total foi de R$ {valor:.2f}")
elif nomeItem == "meu lar":
    valor = (meuLar * duracao) - ((meuLar * duracao) * 10/100)  
    print(f"O valor total foi de R$ {valor:.2f}")
elif nomeItem == "sua mesa":
    valor = (suaMesa * duracao) - ((suaMesa * duracao) * 10/100)  
    print(f"O valor total foi de R$ {valor:.2f}")
else:
    print("item não existe")