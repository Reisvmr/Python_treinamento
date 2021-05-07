#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import socket
import sys
from datetime import datetime

# urllib3.disable_warnings()
#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############

chave = 'LUFRPT1idTV0YWlYbHd5ekozRjNOeE1kVnBHbC9lNUE9eTlGWXNncjJSekRpWE1MZ3hHcDVZYkhka3R5ZmoxSjZDV2RHTWxtOWtTUT0='
url = 'https://10.32.208.101/api/'
#Parametros
type = 'op'
vpn_user = '<show><global-protect-gateway><current-user></current-user></global-protect-gateway></show>'

#Payload contem todos os parametros que seram utilizados no post em forma de dicionario

vpn_user = { 'type': type ,'cmd': vpn_user, 'key': chave}

#Carregando xml para a variavel response
#response = requests.get(url, params=vpn_user, verify=False)
#Converter resultado xml to dict
#dados = xmltodict.parse(response.text)
#Converter resultado para json
#json = json.dumps(dados)
###TESTE FUNCAO
def VPN_DISCOVERY():
    r = response = requests.get(url, params=vpn_user, verify=False)
    dados = xmltodict.parse(response.text)
    lista = dados['response']['result']['entry']
    result_json = []

    for i in lista:
            #if not i['expires'] == 'Never':
                lista = {
                    '{#DOMAIN}': i['domain'],
                    '{#USERNAME}': i['username'],
                    '{#COMPUTER}': i['computer'],
                    '{#COMPUTER}': i['client'],
                    '{#VIRTUAL_IP}': i['virtual-ip'],
                    '{#PUBLIC_IP}': i['public-ip'],
                    '{#LOGIN_TIME_UTC}': i['login-time-utc']
                }
                result_json.append(lista)
    return json.dumps({'data': result_json}, indent=4)
#Imprimindo resultado
#print (json)
#Imprimindo dict
#print (xpars)
#Imprime xml
#print (lista)

################
# Discovery Licenses Operations
#def vpn_user_logon():
#    r = requests.get(url, params=vpn_user, verify=False)
#    dados = dict(xmltodict.parse(r.text))
#    lista = dados['response']['result']['entry']
#    result_json = []
#
print(VPN_DISCOVERY())
