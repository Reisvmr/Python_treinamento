

#DOCUMENTAÇÃO

REFERENCIA
- https://github.com/danidosreis/zabbix_with_python/blob/master/script_paloalto_license.py
- https://github.com/danidosreis/zabbix_with_python/blob/master/script_bigip_certified.py
- https://raw.githubusercontent.com/bezarsnba/zabbix-graylog-monitoring/master/monitoring-graylog.py
- https://github.com/bezarsnba/zabbix-graylog-monitoring


#######################
# GrayLog Node Monitoring Using Zabbix

Template created to monitor GrayLog nodes through LLD (Low Level Discovery)

We added a feature of Zabbix called LLD (Low Level Discovery) in the model, this automation seeks to facilitate the discovery of the nodes in GrayLog, so that you do not have to register the nodes manually just set the time of the discovery rule.

## Monitoring Itens:

* GrayLog: Filter execution Time (FIltered, Incomming, Outgoing, Process)
* GrayLog: Internal Log Message (Error, Fatal, Trace, Warn)
* GrayLog: Journal ( Journal Size)
* GrayLog: Node Memory(LLD)/( Free Memory, Max Memory, Total Memory, Used Memory)
* GrayLog: Node Status (Lifecycle, Processing, Status )
* GrayLog: Services


## Requirements

- Zabbix 4.4 or above;
- PaloAlto 8.1.;
- Python 3.4 or simply Python > 3;
- Imports:
    - import requests
    - import json
    - import sys
    - xmltodict
    - urllib3


## Steps

1. Baixe o arquivo GLOBAL_PROTECT.py e copie-o para a pasta de scripts em seu servidor:

```bash
# cp GLOBAL_PROTECT.py  /etc/zabbix/scripts/
# chmod +x GLOBAL_PROTECT.py
```

2. Crie o token do palo alto (local) com senha e altere as variáveis ​​no arquivo monitoring-graylog.py:

```bash
cat monitoring-graylog.py
url="<URL DO FIREWALL>"
chave = "<Token de Acesso>"
type = 'op'
vpn_user_logon = '<show><global-protect-gateway><current-user></current-user></global-protect-gateway></show>'
vpn_user_logout = '<show><global-protect-gateway><previous-user><gateway>GP-GATEWAY</gateway></previous-user></global-protect-gateway></show>'

## Funções para fazer login no Api Rest e coletar datas ##

def VPN_DISCOVERY_LOGOUT():
    r = response = requests.get(url, params=vpn_user_logout, verify=False)
    dados = xmltodict.parse(response.text)
    lista = dados['response']['result']['entry']
    result_json = []

```

3. Execute o script passando o parâmetro VPN_DISCOVERY_LOGOUT ou VPN_DISCOVERY_LOGON para verificar se está funcionando corretamente:

```bash
# python3.4 monitoring-graylog.py VPN_DISCOVERY_LOGON
{
            "{#DOMAIN}": "verruga",
            "{#USERNAME}": "zille",
            "{#COMPUTER}": "BETO-PC",
            "{#CLIENT}": "Microsoft Windows 10 Pro , 32-bit",
            "{#LOCAL_IP}": "x.x.x.x",
            "{#PUBLIC_IP}": "x.x.x.x",
            "{#LOGIN_TIME_UTC}": "1620647103"
        }
```

4. Check where the * .conf files in the zabbix agent are stored::

```bash
# grep Include /etc/zabbix/zabbix_agentd.conf
Include=/etc/zabbix/zabbix_agentd.conf.d/*.conf
```
5. Copy the file user_parameter_GlobalProtect.conf to the includes directory and change the path of the binary python:

```bash
# cp user_parameter_GlobalProtect /etc/zabbix/zabbix_agentd.conf.d/
# cat user_parameter_GlobalProtect.conf

UserParameter=VPN_DISCOVERY_LOGON,/etc/zabbix/scripts/GLOBAL_PROTECT.py VPN_DISCOVERY_LOGON
UserParameter=VPN_DISCOVERY_LOGOUT,/etc/zabbix/scripts/GLOBAL_PROTECT.py VPN_DISCOVERY_LOGOUT

```
6. Restart zabbix agent

```bash
# systemctl restart zabbix-agent
```

6.Use zabbix_get (from zabbix server) to test some items:

```bash
# zabbix_get -s < IP Agent Zabbix > -k VPN_DISCOVERY_LOGOUT VPN_DISCOVERY_LOGOUT
{
            "{#DOMAIN}": "verruga",
            "{#USERNAME}": "romulo",
            "{#COMPUTER}": "TEL001",
            "{#CLIENT}": "linux-64",
            "{#LOCAL_IP}": "x.x.x.x",
            "{#PUBLIC_IP}": "x.x.x.x",
            "{#LOGIN_TIME_UTC}": "1620397675",
            "{#RESPOSTA}": "client logout"
        }

```