#co = float(input('Comprimento do cateto opsto: '))
#ca = float(input('Comprimeito do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa ira medir {}'.format(hi))

from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa ira medir {}'.format(hi))
