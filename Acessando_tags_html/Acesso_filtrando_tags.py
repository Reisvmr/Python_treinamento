#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:59:56 2019

@author: viniciusreis
"""
############  IMPORTs ################
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen from bs4 import BeautifulSoup html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html') bs = BeautifulSoup(html, 'html.parser') print(bs)

############ VARIAVEIS ###############
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")