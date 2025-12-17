import json

with open('modulo005/funcionarios.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)
print(dados[1]['nome'])