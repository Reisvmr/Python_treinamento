# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:59:57 2019

@author: reisvmr
Ver:1.0
"""
#######Importando Bibliotecas##################
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen 
#################################################
############ Declarando as Variaveis ############
SAU = 'https://is.producao.ccarj.intraer/authenticationendpoint/login.do?RelayState=null&commonAuthCallerPath=%2Fsamlsso&forceAuth=false&passiveAuth=false&tenantDomain=carbon.super&sessionDataKey=ace0fd25-bf57-48c1-85af-ce2f067ca60d&relyingParty=loginunico&type=samlsso&sp=loginunico&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL' # Site 01
SM = 'SITE DO SM' #SITE SM
USER_SAU = '' #Usuário SAU
PW_SAU = ''#Senha SAU
USER_SM = ''#Usuário SM
PW_SM = '' #Senha SM
################################################

#############Inicio do Codigo###################
#    Aplicamos uma requisição para pegar o arquivo HTM
html = urlopen(SAU)

bs = BeautifulSoup(html, 'lxml')

print(bs.div)