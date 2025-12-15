senha = ''

while senha != '1234':
    senha = input('Digite a senha: ')

opcao = 0

while opcao != 4:
    print('\t1-Cadastrar')
    print('\t2-Editar')
    print('\t3-Listar')
    print('\t4-Sair')

    opcao = int(input('Escolha uma opcao: '))
    match opcao:
        case 1:
            print('Cadastrar')
        case 2:
            print('Editar')
        case 3:
            print('Listar')

print('Saiu')