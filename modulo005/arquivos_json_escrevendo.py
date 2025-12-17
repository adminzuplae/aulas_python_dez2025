import json

funcionario = {
    'nome':'Maria'
    ,'sobrenome':'Silva'
    ,'idade':34
    ,'salario':2897.87
    ,'ativo':True
}
with open('modulo005/funcionarios.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

dados.append(funcionario)

with open('modulo005/funcionarios.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4)