
try:
    with open('mensagem.txt','r') as arquivo:
        for linha in arquivo:
            print(linha.strip())
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')