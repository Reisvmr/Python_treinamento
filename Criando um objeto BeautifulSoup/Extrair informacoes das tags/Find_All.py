#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:46:43 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
from urllib.request import urlopen
from bs4 import BeautifulSoup
###############################################
############ Declarando as Variaveis ##########
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")
#############Inicio do Codigo###################
nameList = bs.findAll('span', {'class': 'green'}) # Busscando pela classe css green dentro da chave span

for name in nameList:#Converte a variavel nameListem name
    print(name.get_text())

#Lista todas a Tag de cabecalio do documento.

titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title for title in titles])

# Listo todo o texto independente se e red ou green

allText = bs.find_all('span', {'class':{'green', 'red'}})

print([text for text in allText])
##################################################
######Qauntas ocorrencias da string 
print('Quantas vezes a palavra pequisada aparecea?')
#esquisa = input("Que palavra pesquisar? ")
nameList = bs.find_all(text=pesquisa)
print(len(nameList))
##################################################
title = bs.find_all(id='title', class_='text')
print([text for text in allText])




