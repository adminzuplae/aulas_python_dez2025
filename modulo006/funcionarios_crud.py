import csv, os


arquivo_path = 'modulo006/funcionarios.csv'

def salvar_funcionario(nome, sobrenome, idade, salario, ativo):
    arquivo_existe = os.path.exists(arquivo_path)

    with open(arquivo_path, 'a', newline='', encoding='utf-8') as arquivo:
        campos = ['nome', 'sobrenome', 'idade', 'salario', 'ativo']
        escritor = csv.DictWriter(arquivo, delimiter=';', fieldnames=campos)
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerow({'nome':nome, 'sobrenome':sobrenome, 'idade': idade, 'salario': salario, 'ativo': ativo})

def ler_funcionarios():
    funcionarios = []
    try:
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=';')
            for linha in leitor:
                funcionarios.append(linha)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    return funcionarios