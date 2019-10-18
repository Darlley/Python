codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Informe a quantidade comprada deste produto: "))

if codigo > 0 and codigo < 11:
    preco = 10
elif codigo > 10 and codigo < 16:
    preco = 15
elif codigo > 20 and codigo < 31:
    preco = 20
else:
    preco = 30

preco_total = (preco * quantidade)

if preco_total < 251:
    preco_final = (preco_total*5)/100
elif preco_total > 250 and preco_total < 501:
    preco_final = (preco_total*10)/100
else:
    preco_final = (preco_total*15)/100
    
print("Preço total: R${}".format(preco_final))
