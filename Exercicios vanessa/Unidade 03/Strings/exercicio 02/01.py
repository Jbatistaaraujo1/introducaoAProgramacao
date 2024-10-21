def contemVogal(string):
    vogais = ["a","e","i","o","u"]
    quantVogal = 0
    for i in range(len(vogais)):
        print(i)
        if  vogais[i].lower() in string:
            quantVogal += 1
    if quantVogal >= 1:
        return True
    else:
        return False
   
print(contemVogal("tubo"))