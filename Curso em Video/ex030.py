n = int(input('Digite um número: '))
r = n % 2
if r == 0:
    print('O numero {}{}{} é par!'.format('\33[31m',n,'\033[m'))
else:
    print('O numero {}{}{} é impar!'.format('\33[31m',n,'\033[m'))
