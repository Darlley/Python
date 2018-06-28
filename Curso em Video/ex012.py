p = float(input('Qual o preço? '))

d = p*0.05
pd = p - d

#n = p - (p * 5 / 100)

print('Com 5% de desconto, o valor final é de: R${:.2f}'.format(pd))
