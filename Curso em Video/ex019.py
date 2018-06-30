import random
n1 = str(input('PRIMEIRO ALUNO: '))
n2 = str(input('SEGUNDO ALUNO: '))
n3 = str(input('TERCEIRO ALUNO: '))
n4 = str(input('QUARTO ALUNO: '))
lista = [n1, n2, n3, n4]
a = random.choice(lista)
print('O ALUNO ESCOLHIDO FOI {}'.format(a))
