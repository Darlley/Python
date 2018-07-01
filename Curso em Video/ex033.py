a = int(input('VALOR 1: '))
b = int(input('VALOR 2: '))
c = int(input('VALOR 3: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>c:
    maior = c

print('MENOR: {}'.format(menor))
print('MAIOR: {}'.format(maior))
