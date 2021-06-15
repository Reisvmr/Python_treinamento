#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
pip install requests
pip install simplejson
pip install urllib3
pip install xmltodict
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
#####ARGUMENTOS PARA INPUT
key = sys.argv[1]

#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############

chave = 'LUFRPT1idTV0YWlYbHd5ekozRjNOeE1kVnBHbC9lNUE9eTlGWXNncjJSekRpWE1MZ3hHcDVZYkhka3R5ZmoxSjZDV2RHTWxtOWtTUT0='
url = 'https://10.32.208.101/api/'
###Parametros do Request
type = 'op'
vpn_user_logon = '<show><global-protect-gateway><current-user></current-user></global-protect-gateway></show>'
vpn_user_logout = '<show><global-protect-gateway><previous-user><gateway>GP-GATEWAY</gateway></previous-user></global-protect-gateway></show>'

###Payload contem todos os parametros que seram utilizados no post em forma de dicionario

vpn_user_logon = { 'type': type ,'cmd': vpn_user_logon, 'key': chave}
vpn_user_logout = { 'type': type ,'cmd': vpn_user_logout, 'key': chave}

###FUNCAO QUE COLETA DADOS DA VPN USER LOGON

def VPN_DISCOVERY_LOGON():
    r = response = requests.get(url, params=vpn_user_logon, verify=False)
    dados = xmltodict.parse(response.text)
    lista = dados['response']['result']['entry']
    result_json = []

    for i in lista:
            #if not i['expires'] == 'Never':
                lista = {
                    '{#DOMAIN}': i['domain'],
                    '{#USERNAME}': i['username'],
                    '{#COMPUTER}': i['computer'],
                    '{#CLIENT}': i['client'],
                    '{#LOCAL_IP}': i['virtual-ip'],
                    '{#PUBLIC_IP}': i['public-ip'],
                    '{#LOGIN_TIME_UTC}': i['login-time-utc']
                }
                result_json.append(lista)
    return json.dumps({'data': result_json}, indent=4)

#FUNCAO QUE COLETA DADOS DA VPN USER LOGOUT

def VPN_DISCOVERY_LOGOUT():
    r = response = requests.get(url, params=vpn_user_logout, verify=False)
    dados = xmltodict.parse(response.text)
    lista = dados['response']['result']['entry']
    result_json = []

    for i in lista:
            #if not i['expires'] == 'Never':
                lista = {
                    '{#DOMAIN}': i['domain'],
                    '{#USERNAME}': i['username'],
                    '{#COMPUTER}': i['computer'],
                    '{#CLIENT}': i['client'],
                    '{#LOCAL_IP}': i['virtual-ip'],
                    '{#PUBLIC_IP}': i['public-ip'],
                    '{#LOGIN_TIME_UTC}': i['login-time-utc'],
                    '{#RESPOSTA}': i['reason']
                }
                result_json.append(lista)
    return json.dumps({'data': result_json}, indent=4)

#Teste funcao
#print (VPN_DISCOVERY_LOGOUT())
# Execução argumentos do script 
if key == 'VPN_DISCOVERY_LOGON':
    print(VPN_DISCOVERY_LOGON())

elif key == 'VPN_DISCOVERY_LOGOUT':
    print(VPN_DISCOVERY_LOGOUT())
