#3.10 – Todas as funções: Pensa em algo que você poderia armazenar em
#uma lista. Por exemplo, você poderia criar uma lista de montanhas,
#rios, países, cidades, idiomas ou qualquer outro item que quiser.
#Escreva um programa que crie uma lista contendo esses itens e então
#utilize cada função apresentada neste capítulo pelo menos uma vez.

print('LISTA ORIGINAL')
aleatorio = ['Ler','Comer','Dormir','Estudar','Programar','Debater']
print(aleatorio)
print('\n')

aleatorio.sort()
print(aleatorio)
print('\n')

aleatorio = ['Ler','Comer','Dormir','Estudar','Programar','Debater']
aleatorio.sort(reverse=True)
print(aleatorio)
print('\n')


aleatorio = ['Ler','Comer','Dormir','Estudar','Programar','Debater']
print(sorted(aleatorio))
print(aleatorio)
print('\n')

aleatorio.reverse()
print(aleatorio)
aleatorio.reverse()
print('\n')

print(len(aleatorio))
print('\n')
