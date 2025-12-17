import csv

funcionarios = []

with open('modulo005/funcionarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')
    for linha in leitor:
        funcionarios.append(linha)

print(funcionarios[1]['nome'])