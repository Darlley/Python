horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
salario_Minimo = float(input("Informe o salário mínimo: ")) 
horas_Extras = float(input("Informe o número de hosras extras trabalhadas: "))

# A
a = horas_trabalhadas * salario_Minimo/8

# B
b = horas_Extras * salario_Minimo/4

# C
c =  horas_trabalhadas * a

# D
d = horas_Extras * b

# E
e = c + d

print("O salário a receber é de: R${}".format(e))
