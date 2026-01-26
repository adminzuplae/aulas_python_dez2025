from viacep_service import consulta_por_logradouro

uf = input('Digite um estado(uf): ')
cidade = input('Digite uma cidade do estado informado anteriormente: ')
logradouro = input('Digite um termo para pesquisa do logradouro: ')
resp = consulta_por_logradouro(uf, cidade, logradouro)

print(resp)