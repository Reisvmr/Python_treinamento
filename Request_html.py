# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:53:46 2019

@author: reisvmr
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:59:57 2019

@author: reisvmr
"""
#######Importando Bibliotecas##################
import requests
#################################################
############ Declarando as Variaveis ############
url = 'https://www.youtube.com/results?'
payload = {'search_query':'como fazer chocolate quente'}
################################################
#############Inicio do Codigo###################
r = requests.get(url, params=payload)

print(r.text) # Retorna texto html da pagina
print(r.url) # Retorna a URL da Pagina
