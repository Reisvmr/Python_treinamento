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

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

#Payload contem todos os parametros que seram utilizados no post em forma de dicionario

payload = {'relaxation' : '24455050',
            'tipoCEP' : 'ALL',
             'semelhante':'N'}

response = requests.post(url, data=payload)

#salvando o html
with open('çorreios.html', 'w') as f:
    f.wirite(response.text)

#################################################
#############Inicio do Codigo####################

