# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:07:18 2019

@author: reisvmr
"""
#######Importando Bibliotecas##################
import requests
from bs4 import BeautifulSoup
#################################################
############ Declarando as Variaveis ############
# url Dicionario da linguas uol #####
url = 'http://michaelis.uol.com.br/busca?'
####Variavel da palavra pesquida:
pesquisa = str(input("Oque pesquisar?"))
print (pesquisa)
#####Dados transferidos via dicionario
payload = {'r':'0',
			'f':'0',
			't':'0',
			'palavra': "pesquisa"}
###Cabeçalho requisição simulada.
header = {'(Request-Line)':'GET /busca?r=0&f=0&t=0&palavra=pesquisa HTTP/1.1',
		'Host':	'michaelis.uol.com.br',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Referer':'http://michaelis.uol.com.br/'}
################################################

#############Inicio do Codigo###################



##############################################################




r = requests.get(url, params=payload, headers=header)

soup = BeautifulSoup(r.text, 'lxml')
#Criar uma busca no html baseado no criterio abaixo
div = soup.find('div', {'id':'content'})
#Define que somente o texto desta div sera retornado
print(div.get_text())

with open('michaelis.html', 'w', encoding='utf-8') as f:
	f.write(r.text)

#print(r.request.headers)