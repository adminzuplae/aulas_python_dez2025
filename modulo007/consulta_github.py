import requests

url = f'https://api.github.com/users/'


nome_user = input('Digite o usuário que deseja consultar: ')

response = requests.get(url+nome_user)

if response.status_code == 200:
    dados = response.json()
    print(f'O nome deste usuário é: {dados['name']} e a empresa é: {dados['company']}')
else:
    print('Erro ao acessar a API')