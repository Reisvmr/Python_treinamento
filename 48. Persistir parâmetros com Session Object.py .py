######################Importando Bibliotecas##################
import requests
##############################################################
############        Declarando as Variaveis       ############
##############################################################
url = 'http://www.submarino.com.br/'

s = requests.Session()
s.get(url)
busca = 'notebook'
url = 'http://busca.submarino.com.br/busca.php?q={0}'.format(busca)
##############################################################
############        Inicio  do Codigo             ############
##############################################################

r = s.get(url)
with open('submarino.html', 'w') as f:
	f.write(r.text)