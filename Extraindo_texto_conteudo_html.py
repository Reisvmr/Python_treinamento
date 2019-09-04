# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:38:18 2019

@author: reisvmr
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:59:57 2019

@author: reisvmr
"""
#######Importando Bibliotecas##################
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen 
#################################################
############ Declarando as Variaveis ############
url = 'http://www.decea.gov.br' # Site 01
url2 = 'http://www.google.com.br' # Site 02
################################################

#############Inicio do Codigo###################

#    Aplicamos uma requisição para pegar o arquivo HTM
html = urlopen(url)
html2 = urlopen(url2)
#   Lendo conteudo utilizando o request
#html = requests.get(url)
#    Verifica conteudo 
bs = BeautifulSoup(html, 'lxml')
#   Imprime o conteudo das tags

#Imprime conteudo da tag title

