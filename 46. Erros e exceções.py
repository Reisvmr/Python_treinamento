#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:01:32 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
import requests

url = 'http://google.com/'

try:
    r = requests.get(url, timeout=0.03)	
    #Quando houver respostas HTTP inválidas, as solicitações gerarão uma exceção HTTPError
except requests.exceptions.ConnectionError as e:
	print('ConnectionError')
	#When there are invalid HTTP responses, Requests will raise an HTTPError exception
except requests.exceptions.HTTPError as e:
	print ('HTTPError')
	#Se o pedido atingir o tempo limite, esta exceção será gerada
except requests.exceptions.Timeout as e:
	print ('Timeout')
    # Talvez esteja configurado para uma nova tentativa ou continue em um loop de nova tentativa
except requests.exceptions.TooManyRedirects as e:
	print ('TooManyRedirects')
    # Informe ao usuário que o URL estava incorreto e tente outro.
except requests.exceptions.RequestException as e:
    # erro catastrófico. fiança.
	print ('RequestException')
