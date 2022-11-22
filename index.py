#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import *
import os

#Exibe um histórico com todas as equipes e nomes criadas nos arquivos equipes_um,equipes_dois,equipes_tres
def exibir_historico():
	try:
		with open("historico.txt", "r") as arquivo:
			result = arquivo.read()
	except FileNotFoundError: #Verifica se o arquivo existe
		return ("Arquivo não encontrado")
	else:
		return result

#Função que vai verificar a opção recebida e retornar a leitura de um dos 3 arquivos com as equipes e membros
def exibir_equipes(opc):
	try:
		if opc == '3':
			with open("equipes_um.txt", "r") as arquivo:
				result = arquivo.read()
		elif opc == '4':
			with open("equipes_dois.txt.txt", "r") as arquivo:
				result = arquivo.read()
		elif opc == '5':
			with open("equipes_tres.txt", "r") as arquivo:
				result = arquivo.read()
	except FileNotFoundError: #Verifica se o arquivo existe
		return ("Arquivo não encontrado")
	else:
		return result

#Função responsavel por adicionar todos os usuarios e quipes em um arquivo unico chamado historico.txt
def add_historico(nome_equipe,user1,user2='',user3=''):
	with open("historico.txt", "a") as arquivo:
		arquivo.write(nome_equipe + " | " + user1 + " | " + user2 + " | " + user3 + "\n")

#Funçao que adiciona 1 equipe e 1 pessoa
def add_equipes_um(nome_equipe,user1):

	with open("equipes_um.txt", "a") as arquivo:
		arquivo.write(nome_equipe + " | " + user1 + " | ")

#Funçao que adiciona 1 equipe e 2 pessoas
def add_equipes_dois(nome_equipe,user1,user2):
	with open("equipes_dois.txt", "a") as arquivo:
		arquivo.write(nome_equipe + " | " + user1 + " | " + user2)

#Funçao que adiciona 1 equipe e 3 pessoas
def add_equipes_tres(nome_equipe,user1,user2,user3):
	with open("equipes_tres.txt", "a") as arquivo:
		arquivo.write(nome_equipe + " | " + user1 + " | " + user2 + " | " + user3)

#Função que vai adicionar o total de respostas
def totalizador():
	final = 0
	try:
		with open("historico.txt", "r") as arquivo:
			
			result = arquivo.readlines()
			for y in result:
				final += 1
			
			with open("totalizador.txt", "w") as file:
				file.write(str(final))
			
			with open("totalizador.txt", "r") as filess:
				resultado = filess.read()

	except FileNotFoundError:
		return "Arquivo vazio ou não encontrado"
	else:
		return "{} Resposta(s) adicionadas".format(resultado)
			
			
def delete_all_files():
	for file in os.listdir(os.getcwd()):
		if file.endswith(".txt"):
			os.remove(file)
	
	#if os.path.exists("equipes_dois.txt") or os.path.exists("equipes_tres.txt") or os.path.exists("equipes_.txt"):
	#	os.remove("equipes_dois.txt")
	#	return "Arquivos deletados"
	else:
		return "Arquivos não encontados"
		

