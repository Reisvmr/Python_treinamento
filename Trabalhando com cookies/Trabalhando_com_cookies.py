#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
import requests
#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
url = 'http://pythonscraping.com/pages/processing.php/'
cookie = r.cookies.get_dict()

#############Inicio do Codigo####################
r = requests.post(url, data=params)
print(r.text)

print(cookie)