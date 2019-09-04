
# -*- coding: utf-8 -*-
#######Importando Bibliotecas##################

#Aula 11 Usando timeout
import requests

#mostrar que o timeout é um tempo limite de requests, caso ultrapasse esse tempo de espera
#retornara um erro.
r = requests.get('http://google.com', timeout=(0.03,1))

#If the remote server is very slow, you can tell Requests to wait forever for a response, 
#by passing None as a timeout value and then retrieving a cup of coffee.
r = requests.get('http://google.com', timeout=None)

#The timeout value will be applied to both the connect and the read timeouts. 
#Specify a tuple if you would like to set the values separately:
r = requests.get('http://google.com', timeout=(3.05, 27))


