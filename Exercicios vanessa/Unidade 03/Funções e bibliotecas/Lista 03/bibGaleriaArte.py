import random

def consultaPreco (obra):
    return random.randint(2,8) * random.choice([132.40, 275.81, 98.66])

def consultaArtista (obra):
    nome = random.choice(["Manoel Gomes", "Dênis Novaes", "Adélia Machado", "Patrícia Lisboa", "Leonardo Resende"])    
    return nome

def consultaQuantObras (artista):
    return random.randint(0,5)

def consultaTipo (obra):
    return random.choice(["Quadro", "Escultura"])