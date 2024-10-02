# a) Uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne verdadeiro se ele for múltiplo de 4, ou falso caso contrário.

def testaMultiplo4(inteiro):
    if inteiro % 4 == 0:
        return True
    else:
        return False

# b) Uma função contaDivisores que receba como parâmetro um número inteiro, e retorne a quantidade de divisores que ele tem. (Dica: lembre-se de que não é possível dividir por zero)
def contaDivisores(inteiro):
    divisores = 0
    for i in range(1,inteiro):
        if inteiro % i == 0:
            divisores += 1
    return divisores

