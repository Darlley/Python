from datetime import date
a = int(input('Em que ano: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Bissexto")
else:
    print('Não é bissexto')
