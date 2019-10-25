l1 = ["fusca", "corola", "virtus", "fluence", "gol", "fox", "uno"]
l2 = [62000, 50000, 35000, 32000, 10000, 2000, 27000]

# 1
l1.append("fusion")
l1.append("opala")
l1.append("sandero")

# 2
del l2[5]

# 3
l3 = l1 + l2

# 4
l1.sort()
l2.sort()

# 5
nome = input("Informe um nome: ")
valor = int(input("Informe um valor: "))

l1.remove(nome)
l2.remove(valor)
