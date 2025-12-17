import csv

with open('modulo005/produto.csv', 'a', newline='', encoding='utf-8') as arquivo:
    campos = ['nome', 'preco']
    escritor = csv.DictWriter(arquivo, delimiter=';', fieldnames=campos)
    escritor.writeheader()
    escritor.writerow({'nome':'Notebook', 'preco':3599.88})
    escritor.writerow({'nome':'Mouse', 'preco':149.99})
