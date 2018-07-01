from random import randint
compu = randint(0,5)
print('-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
jog = int(input('EM QUE NÚMEREO PENSEI? '))
if compu == jog:
    print('PARABÉNS!!!')
else:
    print('VOCÊ ERROU!!! Eu pensei em {}'.format(compu))
