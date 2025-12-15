nomes = ['Maria', 'Joao', 'Jose']

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])

funcionario = {
    'nome':'Maria'
    ,'sobrenome':'Silva'
    ,'idade':34
    ,'salario':2897.87
    ,'ativo':True
}

for chave, valor in funcionario.items():
    print(chave, valor)

for indice, nome in enumerate(nomes):
    print(indice, nome)