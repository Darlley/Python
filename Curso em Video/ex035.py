a = float(input('Tamanho 1: '))
b = float(input('Tamanho 2: '))
c = float(input('Tamanho 3: '))
if a < b + c and b < a + c and c < a + b:
    print('PODEM FORMAR TRIANGULO')
else:
    print('Não podem formar triangulo!')
