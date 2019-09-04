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

##############################################################
############ Declarando as Variaveis  de Conecxao ############
##################SAU CONEXAO#################################
SAU = 'https://is.producao.ccarj.intraer/sau/' # Site 01
USER_SAU = '' #Usuário SAU
PW_SAU = ''#Senha SAU
##############################################################
######Aceitar certificado como valido#########################
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
##############################################################

#################### SM CONEXAO ##############################
SM = 'SITE DO SM' #SITE SM
USER_SM = ''#Usuário SM
PW_SM = '' #Senha SM

#############Inicio do Codigo###################
#    Aplicamos uma requisição para pegar o arquivo HTM
html = urlopen(SAU)
#html2 = urlopen(SM)
#html = urllib.request.urlopen(SAU)
bs = BeautifulSoup(html, 'lxml')

print(bs.div)
