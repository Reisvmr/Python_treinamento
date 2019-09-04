# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:59:57 2019

@author: reisvmr
"""
#######Importando Bibliotecas##################
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
#################################################
############ Declarando as Variaveis ############
#Declara o link da url que iremos analizar.
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#Faz o parser ('html.parser') e Converte a url em uma varial chamda bs (.read = leitura) 
bs = BeautifulSoup(html.read(), 'html.parser')


################################################

#############Inicio do Codigo###################
#Testa a pagina e se nenhum erro ocorrer esecuta o comando.
try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())

##############################################################
    































