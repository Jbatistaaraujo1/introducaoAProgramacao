def testeVogal(caractere):
    vogais = ["A", "Á", "Â", "Ã", "À", "E", "É", "Ê", "I", "Í", "O", "Ó", "Õ", "Ô", "U", "Ü"]
    if caractere.upper() in vogais:
        return True
    else:
        return False 