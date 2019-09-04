# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:59:57 2019

@author: reisvmr
"""
#######Importando Bibliotecas##################
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from urllib.request import urlopen 

#################################################
############ Declarando as Variaveis ############
url = 'http://www.decea.gov.br' # Site 01
################################################

#############Inicio do Codigo###################
#    Aplicamos uma requisição para pegar o arquivo HTM
html = urlopen(url)

#   Lendo conteudo utilizando o request em pagina web #####

"""
############ aplica get.request na url designada####

html = requests.get(url)
"""

#####  Verifica conteudo ######
#bs = BeautifulSoup(html, 'lxml') #get em tempo real da pagina
#   Imprime o conteudo das tags

""" #Inicio do Comentario
#Imprime conteudo das tag 

print(bs.title)#Imprime conteudo da tag title
print(bs.head)
print(bs.dir)
print(bs.img)
print(bs.input)
print(bs)
print(bs.h1)
print(bs.address)
print(bs.link)
print(bs.base)
print(bs.header)
print(bs.div)

""" #Fim do Comentario


""" #Inicio 2 comentario
#######Abrindo segunda pagina do curso de Webscraping###

#with open('arquivo.html', 'r') as f:
#    bs = BeautifulSoup(f, 'html5lib')

######################Lendo conteudo#####################

#tag = bs.title
#print(bs.prettify['class'])
#print(bs.a['href'])
#print(bs.prettify())
#print(bs.get_text()) # retorna texto de todas as Tag
#print(bs.p.get_text()) #retorna o conteudo da tag p e seu filhos
#print(bs.p.string()) # retorna o texto da Tag p somente.
#print(bs.p.b.string())
#Abrindo segunda pagina do curso de Webscraping


""" #Fim do segundo comentario


""" #INICIO DO TERCEIRO COMENTARIO
###########################################################
############## NAVEGANDO USANDO TAGS#######################
###########################################################

with open('arquivo02.html', 'r') as f:
    bs = BeautifulSoup(f, 'lxml')
    
#print(bs.title) #Imprime titulo da pagina
#print(bs.head) # Imprime o cabrçalho da pagina
#print(bs.head.title)# Imprime o titulo dendro do head
#print(bs.a) # Mostra o primeiro link de um site
#print(bs.img) # Mostra imagens 
print(bs.td) #Mostra  tabela HTML simple
print(bs.tr) #Mostra linha da tabela
###########################################################
""" #FIM TERCEIRO COMENTARIO

###########################################################
######### NAVEGANDO NOS FILHOS DE UMA TAG #################
###########################################################

with open('arquivo02.html', 'r') as f:
    bs = BeautifulSoup(f, 'lxml')

#print(bs.table.contents) # usando o "contants" mostra conteudo de uma tabela
#print(type(bs.contents)) # Mostra tipo da lista
#print(len(bs.contents)) # conta linhas de uma lista
#print(bs.table.contents[1]) # mostra segunda linha da tabela

#############Condição#############################
#   Mostra linhas da tabela que contenham a seguinte string 'tr'
"""
for child in bs.table.contents:
        if child.name == 'tr':
            print(child)


    
for child in bs.footern.p.children:
    if child.name == 'a':
        print(child.get('href))

print(len(list(bs.decendants)))
"""
##############################################################
######### NAVEGANDO NOS FILHOS DE UMA TAG P2 #################
##############################################################

"""
for tag in bs.decendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)
"""
"""
for tag in bs.descendants:
    if isinstance(tag, Tag):
        print(tag)
"""
##############################################################
######## diferença entre strings e stripped_strings ##########
##############################################################
#String: interage com todas as strings dependentes           #
#stripped_strings: Remove espaços extras trazendo o          #
#conteudo principal.                                         #
##############################################################
"""
for string in bs.aside.string:
    print(repr(string)) #repre =converte para volores legibes no python
    
"""
for string in bs.aside.striped_strings:
    print(repr(string))



##############################################################
######### NAVEGANDO NOS PAIS DE UMA TAG P1 ###################
##############################################################
    































