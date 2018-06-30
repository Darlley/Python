from random import shuffle
#import random
a = str(input('PRIMEIRO NOME: '))
b = str(input('SEGUNDO NOME: '))
c = str(input('TERCEIRO NOME: '))
d = str(input('QUARTO NOME: '))
lista = [a, b, c, d]
#ACERTEI ATÉ AQUI

shuffle(lista)
#random.shuffle(lista)
print(lista)
