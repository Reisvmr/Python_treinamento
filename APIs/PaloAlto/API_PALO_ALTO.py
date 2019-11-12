"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
pip install requests
pip install simplejson
pip install urllib3
"""
#######Importando Bibliotecas##################
import requests
import json
import urllib3
import xmltodict
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# urllib3.disable_warnings()
#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############

chave = 'LUFRPT1idTV0YWlYbHd5ekozRjNOeE1kVnBHbC9lNUE9eTlGWXNncjJSekRpWE1MZ3hHcDVZYkhka3R5ZmoxSjZDV2RHTWxtOWtTUT0='
categoriaurl = 'https://10.32.208.101/api/?type=report&async=yes&reporttype=predefined&reportname=top-url-categories&'
#Payload contem todos os parametros que seram utilizados no post em forma de dicionario

payload = { 'key' : chave}


#Carregando xml para a variavel response
response = requests.get(categoriaurl, params=payload, verify=False)
#Converter resultado xml to dict
xpars = xmltodict.parse(response.text)
#Converter resultado para json
json = json.dumps(xpars)
#Imprimindo resultado
print (json)
