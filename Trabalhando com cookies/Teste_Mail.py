#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:27:33 2019

@author: viniciusreis
"""
#######Importando Bibliotecas##################
import requests
from selenium import webdriver
##############################################################
############        Declarando as Variaveis       ############
##############################################################
driver = webdriver.Firefox()
url = "https://192.168.0.23:10443/admin/9523e22d6e1f0748e237fbe88862bd47/pt_BR/html/Login.html" #a redirect to a login page occurs
driver.get(url) #the login page is displayed
############ Declarando as Variaveis  de Conecxao ############
#making a persistent connection to authenticate
params = {'credential_0':'reisvmr', 'credential_1':'shakall1984'}
s = requests.Session()
resp = s.post(url, params) #I get a 200 status_code

#passing the cookies to the driver
driver.add_cookie(s.cookies.get_dict())
