from calculos import soma, subtracao, multiplicacao, divisao

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

so = soma(numero1, numero2)
su = subtracao(numero1, numero2)
mu = multiplicacao(numero1, numero2)
di = divisao(numero1, numero2)

print(so, su, mu, di)