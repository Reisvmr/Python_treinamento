#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:01:32 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
import requests
##############################################################
############        Declarando as Variaveis       ############
##############################################################

url = 'http://compras.dados.gov.br' # esta variavel equivale a {0}
cnpj = '07689002000189' #Embraer ## esta variavel equivale a {1}

url = '{0}/contratos/v1/contratos.json?cnpj_contratada={1}'.format(url, cnpj)

r = requests.get(url)
print(r.json())
print(r.json()['_embedded']['contratos'])
print(r.json()['_embedded']['contratos'][0])