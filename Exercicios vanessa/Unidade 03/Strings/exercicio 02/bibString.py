def RemoveVogais(string):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    novaString = ""
    for i in range(len(string)):
        if string[i].lower() not in vogal:
            novaString += string[i]
    return novaString
            