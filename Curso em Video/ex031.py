d = float(input('Qual a distância da viajem: '))
p = d * 0.50 if d <= 200 else 0.45*d
#if d <= 200:
#    p = 0.50 * d
#else:
#    p = 0.45 * d
print('O valor da viaje, custa: {}'.format(p))
