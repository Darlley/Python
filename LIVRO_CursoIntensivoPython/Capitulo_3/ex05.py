#3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
#convidados não poderá comparecer ao jantar, portanto será necessário enviar um
#novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
#• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
#no final de seu programa, especificando o nome do convidado que não poderá
#comparecer.
#• Modifique sua lista, substituindo o nome do convidado que não poderá
#comparecer pelo nome da nova pessoa que você está convidando.
#• Exiba um segundo conjunto de mensagens com o convite, uma para cada
#pessoa que continua presente em sua lista.

convidados = ['Alvin Plantinga', 'William Lane Craig', 'Alister McGrath']
mensagem_saudação = "Olá senhor "
mensagem_convite = ".\nGostaria muito de sua presença em meu jantar.\n"
del convidados[2]
print(convidados)

print(mensagem_saudação+convidados[0].title()+mensagem_convite)
print(mensagem_saudação+convidados[1].title()+mensagem_convite)

convidados.append('Francis Collins')
novo_convidado = convidados[2]
print(mensagem_saudação + novo_convidado+mensagem_convite+".")
