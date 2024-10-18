def contemVogal(string):
    vogais = ["a","e","i","o","u"]
    quantVogal = 0
    for i in range(len(string)):
        if  string[i].lower() in vogais:
            quantVogal += 1
        if quantVogal == 0:
            print("False")
        else:
            print("True")
   
contemVogal("joao")