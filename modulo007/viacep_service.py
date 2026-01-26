import requests

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if dados.get('erro'):
            raise Exception('CEP inexistente')
        return dados
    elif response.status_code == 400:
        raise Exception('CEP no formato incorreto')
    else:
        raise Exception('Erro ao acessar a API ViaCEP')
    
def consulta_por_logradouro(uf, cidade, logradouro):
    url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if len(dados) == 0:
            raise Exception('Dados inexistente')
        return dados
    elif response.status_code == 400:
        raise Exception('Dados no formato incorreto')
    else:
        raise Exception('Erro ao acessar a API ViaCEP')
    