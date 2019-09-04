# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:50:25 2019

@author: reisvmr
"""
#Importando Bibliotecas necessarias
from bs4 import BeautifulSoup
import requests
#Abrndo arquivo html com permição de leitura e tranforma-lo em uma variavel chamada f
"""#########Abrindo pagina e imprimindo o código.############
 with open('arquivo.html','r') as f:
       soup_string = BeautifulSoup(f.read(),'html.parser')
 print(soup_string)
"""############Final da P1#############
###########Abrindo pagina e imprimindo o codigo#Utilizando o lxml para fazer o parser######
r = requests.get('https://www.decea.gov.br')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
##################################################
"""######Utilizando o HTML5_lib para fazer o parser#####
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')

print(soup_string)
"""#####################################################
