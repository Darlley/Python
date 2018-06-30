km = float(input('Quantos KM foi percorrido? '))
dia = int(input('Quantos dias foi alugado? '))

pd = 60 * dia

print('Por dia, o aluguel custa R$60, como foi alugado por {}, você tem a pagar 60 x {} = {}'.format(dia, dia, pd))

pk = 0.15 * km

print('Cada Km custa R$0.15, como foi alugado por {}, você tem a pagar também 0.15 x {} = {}'.format(km, km, pk))

t = pd + pk

print('Somando-se os dois valores a ser pago, o total que esta devendo é {}'.format(t))
