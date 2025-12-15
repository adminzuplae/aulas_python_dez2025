def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    if n2 > 0:
        resultado = n1 / n2
        return resultado

def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total