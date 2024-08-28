servico = str(input("Escreva o tipo de serviço: "))
quanFolhas = int(input("Escreva a quantidade de folhas: "))

pretoBranco = 0.06
colori = 0.29

if (servico == "Xérox"):
   cor = str(input("Qual a cor? "))
   if (cor == "PB"):
     valor = quanFolhas * pretoBranco
     print(f"Valor: R$ {valor:.2f}")
   elif( cor == "Colorida"):
      valor = quanFolhas * colori
      print(f"Valor: R$ {valor:.2f}")
elif(servico == "Encadernação"):
    if (quanFolhas <= 100):
      valor = 2
      print(f"Valor: R$ {valor:.2f}")
    elif(quanFolhas > 100):
      valor = 4
      print(f"Valor: R$ {valor:.2f}")