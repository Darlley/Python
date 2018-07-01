s = float(input('Qual o salário do funcionario? R$'))
if s <= 1250:
    a = s + (s * 15 / 100)
else:
    a = s + (s * 10 / 100)
print('O salário passa a ser de R$', a)
