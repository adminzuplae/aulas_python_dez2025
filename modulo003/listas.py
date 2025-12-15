nomes = ['Maria', 'Joao', 'Jose']
numeros = [20,15]
numeros.append(10)

print(nomes)

print(len(nomes))

print(nomes[0])
print(nomes[-1])

nomes[1] = 'Marcos'
print(nomes)

nomes.append('Joaquina')
print(nomes)

nomes.remove('Maria')
print(nomes)

nomes.pop(-1)
print(nomes)

print(numeros)