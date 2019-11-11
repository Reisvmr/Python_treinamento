#!/usr/bin/env python2

"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
import requests
import urllib3
#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############

chave = 'LUFRPT1idTV0YWlYbHd5ekozRjNOeE1kVnBHbC9lNUE9eTlGWXNncjJSekRpWE1MZ3hHcDVZYkhka3R5ZmoxSjZDV2RHTWxtOWtTUT0='
categoriaurl = 'https://10.32.208.101/api/?type=report&async=yes&reporttype=predefined&reportname=top-url-categories&'
#Payload contem todos os parametros que seram utilizados no post em forma de dicionario

payload = { 'key' : chave}


#print(response.get_text())
r = requests.get(categoriaurl, params=payload, verify=False)

#################################################
#############Inicio do Codigo####################
print (r.text)
#print (r.url)
