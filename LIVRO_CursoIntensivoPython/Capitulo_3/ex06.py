#3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
#portanto agora tem mais espaço disponível. Pense em mais três convidados para o
#jantar.
#• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
#uma instrução print no final de seu programa informando às pessoas que você
#encontrou uma mesa de jantar maior.
#• Utilize insert() para adicionar um novo convidado no início de sua lista.
#• Utilize insert() para adicionar um novo convidado no meio de sua lista.
#• Utilize append() para adicionar um novo convidado no final de sua lista.
#• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
#está em sua lista.

convidados = ['Alvin Plantinga', 'William Lane Craig', 'Francis Collins']
print(convidados[0]+", "+convidados[1]+", "+convidados[2]+".\nConsegui uma mesa maior e convidei mais pessoas a nos acompanhar.\n")

convidados.insert(0, "John Walton")
convidados.insert(2, "Bertrand Russell")
convidados.append("Leibniz")

print(convidados)

mensagem_saudação = "Olá senhores "
mensagem_convite = ".\nGostaria muito da presença dos senhores em nosso jantar.\n"

print("\n"+mensagem_saudação + convidados[0] + ", " + convidados[2] + " e " + convidados[5]+mensagem_convite)
