opcao = 15

match opcao:
    case 1:
         print('Cadastrar')
    case 2:
        print('Editar')
    case 3:
        print('Listar')
    case 4:
        print('Deletar')
    case 0:
        print('Voltar ao menu principal')
    case _:
        print('Opcao invalida')

comando = 'inicio'

match comando:
    case 'start':
        print('Iniciando')
    case 'stop':
        print('Parando')
    case _:
        print('Comando invalido')