import json

try:
    with open('modulo005/funcionarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')
except json.JSONDecodeError:
    print('Erro no formato do JSON')
else:    
    print(dados)
    print(dados[1]['nome'])