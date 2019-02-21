#3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
#• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
#• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.
#• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
#• Mostre que sua lista manteve sua ordem original exibindo-a.
#• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
#• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
#• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
#• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
#• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
#• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

visitar = ['Amazônia', 'Madagascar', 'Uruguai', 'Peru', 'Caribe']
print(visitar)

#1º ALTERAÇÃO
print("#1º ALTERAÇÃO")
print(sorted(visitar))
print(visitar)
print("\n")
#2º ALTERAÇÃO
print("#2º ALTERAÇÃO")
print("SEM SUCESSO")
print("\n")
#3º ALTERAÇÃO
print("#3º ALTERAÇÃO")
visitar.reverse()
print(visitar)
print("\n")
#4º ALTERAÇÃO
print("#4º ALTERAÇÃO")
visitar.reverse()
print(visitar)
print("\n")
#5º ALTERAÇÃO
print("#5º ALTERAÇÃO")
visitar.sort()
print(visitar)
print("\n")
#6º ALTERAÇÃO
print("#6º ALTERAÇÃO")
visitar.sort(reverse=True)
print(visitar)
print("\n")
#7º ALTERAÇÃO
print("#7º ALTERAÇÃO")
print("\n")
#8º ALTERAÇÃO
print("#8º ALTERAÇÃO")
print("\n")
