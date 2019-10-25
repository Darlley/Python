a = [1, 2, 3, 4, 5, 6, 10]
b = [10, -1.3, 58, 100, -20]

# 1
len(a)
len(b)

# 2
a.insert(5, 12)
b.insert(5, 12)

# 3
valor = int(input("Informe um valor: "))

i = 0
tamanho = len(a)

for i in range(tamanho):
    if valor == a[i]:
        print(i)
    if valor == b[i]:
        print(i)

# 4
a.sort()
b.sort()

# 5
i = 0
tamanho = len(a)

for i in range(tamanho):
    b.append(a[i])
