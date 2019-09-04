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
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
