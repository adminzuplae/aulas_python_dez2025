def saudacao(nome):
    print(f'Ola, {nome}')

def soma(n1, n2):
    soma = n1 + n2
    print(soma)

def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total

def verificar_maioridade(idade):
    if idade >= 18:
        return 'Pode entrar'
    else:
        return 'Nao pode entrar'
    

saudacao('Joao')
saudacao('Maria')

soma(10,5)
soma(5,15)

total = calcular_total(15.99, 5)
print(total)

print( verificar_maioridade(17) )
