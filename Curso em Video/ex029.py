v = float(input('QUALA VELOCIDADE? '))
#s = v - 80
#m = s * 7
m = (v-80)*7
if v>=80:
    print('VOCÊ excedeu a velocidade! Sua multa é de {}'.format(m))
else:
    print('Dirija com segurança! :)')
