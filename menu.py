#!/usr/bin/python
# -*- coding: utf-8 -*-
from index import *

flag = True
while flag:
	opc = input('''
============= Competição de Programação BSI-2022 =============
[ 1 ] - Adicionar equipe
[ 2 ] - Histórico de arquivos
[ 3 ] - Listar equipes com 1 pessoa
[ 4 ] - Listar equipes com 2 pessoas
[ 5 ] - Listar equipes com 3 pessoas
[ 6 ] - Totalizador
[ 7 ] - delete all files
[ 8 ] - Sair
>>''')

	if opc == '8':
		flag = False

	elif opc == '1':
		nome_equipe = input("Digite o nome da sua equipe: ")
		numero_participantes = int(input("Informe quantos integrantes irão participar na equipe. (1 a 3): "))


		if numero_participantes == 1:
			user1 = input("Digite o nome do participante: ")
			add_equipes_um(nome_equipe,user1)
			add_historico(nome_equipe,user1)

		elif numero_participantes == 2:
			user1 = input("Digite o nome do primeiro participante: ")
			user2 = input("Digite o nome do segundo participante: ")
			add_equipes_dois(nome_equipe,user1,user2)
			add_historico(nome_equipe,user1,user2)

		elif numero_participantes == 3:
			user1 = input("Digite o nome do primeiro participante: ")
			user2 = input("Digite o nome do segundo participante: ")
			user3 = input("Digite o nome do terceiro participante: ")
			add_equipes_tres(nome_equipe,user1,user2,user3)
			add_historico(nome_equipe,user1,user2,user3)

	elif opc == '2':
		print(exibir_historico())

	elif opc == '3':
		print("============= Equipes com 1 pessoa =============")
		print(exibir_equipes(opc))

	elif opc == '4':
		print("============= Equipes com 2 pessoa =============")
		print(exibir_equipes(opc))

	elif opc == '5':
		print("============= Equipes com 3 pessoa =============")
		print(exibir_equipes(opc))

	elif opc == '6':
		print(totalizador())

	elif opc == '7':
		print(delete_all_files())