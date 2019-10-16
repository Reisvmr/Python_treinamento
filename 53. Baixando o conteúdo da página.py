#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:27:33 2019

@author: viniciusreis .
"""
######################Importando Bibliotecas##################
import requests
from bs4 import BeautifulSoup
##############################################################
############        Declarando as Variaveis       ############
##############################################################
def get_http(url, nome_livro):

	nome_livro = nome_livro.replace(' ', '%20') # se o nome do livro tiver espasso subistitua por %20'
	url = '{0}?q={1}'.format(url, nome_livro)

	try:
		return requests.get(url)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
				requests.excepetions.ConnectionError, requests.exceptions.Timeout) as e:
		print(str(e))
		pass
	except Exception as e:
		raise

if __name__ == '__main__':

	url = 'http://busca.saraiva.com.br/'
	nome_livro =input ('Qual Livro buscar ? ')

	r = get_http(url, nome_livro)

	with open('result.html', 'w') as f:
		f.write(r.text)