nome = 'Maria'
sobrenome = 'Silva'
idade = 34
salario = 2897.87
ativo = True

funcionario = {
    'nome':'Maria'
    ,'sobrenome':'Silva'
    ,'idade':34
    ,'salario':2897.87
    ,'ativo':True
}
print(funcionario)

print(funcionario['nome'])
funcionario['nome'] = 'Joaquina'

print(funcionario)

del funcionario['ativo']

print(funcionario)

funcionario['endereco'] = 'Rua Getulio, 20'
print(funcionario)