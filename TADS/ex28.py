cidade = []
i= 0
total_Salario = 0.0

qtd = int(input("Quantos habitantes: "))
salario = float(input("Informe o salário: "))
salario_Anterior = salario
filhos = int(input("Informe a quantidade de filhos: "))
total_filhos = filhos

maior = salario
menor = salario

for i in range(qtd-1):
    salario = float(input("Informe o salário: "))
    total_Salario = total_Salario + salario

    if salario_Anterior > salario:
        maior = salario_Anterior
    if salario_Anterior <salario:
        menor = salario
        
    salario_Anterior = salario
    
    filhos = int(input("Informe a quantidade de filhos: "))
    total_filhos += filhos

media_Salario = total_Salario/qtd
media_Filhos = total_filhos/qtd

print("Média salário: {}".format(media_Salario))
print("Média número de filhos: {}".format(media_Filhos))
print("Maior salário: {}".format(maior))
