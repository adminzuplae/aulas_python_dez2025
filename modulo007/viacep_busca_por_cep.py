from viacep_service import consulta_cep

cep = input('Digite um cep: ')
resp = consulta_cep(cep)

print(resp)