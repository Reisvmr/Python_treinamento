#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################

import requests # Import requests
from bs4 import BeautifulSoup # Import BS4
############ Declarando as Variaveis ############
url = 'http://www.google.com/' 
#############Inicio do Codigo###################

r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
	print('Çontinua programa')
    #soup = BeautifulSoup(r.text, 'html.parser')

print(r.request.headers)