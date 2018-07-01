nome = str(input('Qual su nome? '))
print('Olá {}, seja bem vindo!'.format(nome))
print('Vamos calcular sua média!')
n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
m = (n1+n2)/2
if m <= 5:
    print('{}, sua média foi {:.1f} e infelizmente é insuficiente!'.format(nome, m))
else:
    print('{}, sua média foi de {} e é suficiente, Parabéns!'.format(nome, m))

print('=MÉDIA CALCULADA COM SUCESSO=')
