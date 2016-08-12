#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#
# Esse script foi desenvolvido para facilitar o cadastro um ou mais hosts no Zabbix, 
# Permitindo uma ótima facilidade e agilidade, utilizando um arquivo no formato
# CSV, como exemplo: rel_grupo.csv
#
# Este arquivo de exemplo em formato CSV, cadastra 50 equipamentos em apenas 20 segundos em dois servidores zabbix
# Inserindo o arquivo .csv os seguintes parametros: host, ip e grupo
# Versão da API 2.1
#
# Author: Vinicius Trancoso Bitencourt - <https://github.com/viniciustbitencourt>
# FileName: cadastrar_hosts.py
# FileCSV: rel_grupo.csv
# License: MIT License

import csv
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

#Modificar parametros de configuracao no arquivo conf.ini
config = SafeConfigParser()
config.read('conf.ini')

#Coleta os valores das variaves do arquivo conf.ini - Servidor 01 Zabbix
host01 = config.get('zabbix01', 'hostname')
usr01 = config.get('zabbix01', 'user')
pwd01 = config.get('zabbix01', 'passwd')

#Coleta os valores das variaves do arquivo conf.ini - Servidor 01 Zabbix
host02 = config.get('zabbix02', 'hostname')
usr02 = config.get('zabbix02', 'user')
pwd02 = config.get('zabbix02', 'passwd')

#Relatorio CSV
rel = config.get('relatorio', 'csv')

#Autenticacao cada Server
zapi = ZabbixAPI(host01)
zapi2 = ZabbixAPI(host02)

#Hostname e Password - Criar Perfil de usuario Escrita e Leitura no Servidor Zabbix
zapi.login(usr01, pwd01)
zapi2.login(usr02, pwd02)

class CadastrarHosts(object):
	pass
	#Leitura do arquivo rel_grupo.csv com delimitador ;
	f = csv.reader(open(rel), delimiter=';')

	#Loop para coleta das colunas no arquivo
	for y in f:
		a ='%s' % y

		#Realiza outro Loop pra separar os indices - Foreach em Python
		for (i, a, b) in f:
			i, a, b
			#Print do cadastro do equipamento um a um
			print 'cadastrando equipamento - %s' % i

			#Coleta os Ids, de cada servidor
			group_id = zapi.hostgroup.get({"filter": {"name" : b}})[0]['groupid']
			group_id2 = zapi2.hostgroup.get({"filter": {"name" : b}})[0]['groupid']
			
			#Cadastra os hosts com o template ICMP Ping, se for cadastrar com o outro template, alterar abaixo
			template_id = zapi.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']
			template_id2 = zapi2.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']

			#Cadastra o equiapamento no Servidor 01
			zapi.host.create(
			{	
				"host":i,
					"interfaces":[{
					"type": 1,
					"main":1,
					"useip":1,
					"ip":a,
					"dns":"",
					"port":"10050"
				}],
				"groups" : [{"groupid": group_id}],
				"templates" : [{"templateid": template_id}],
			})
			#Cadastra o equipamento no Servidor 02
			zapi2.host.create(
                        {
                                "host":i,
                                        "interfaces":[{
                                        "type": 1,
                                        "main":1,
                                        "useip":1,
                                        "ip":a,
                                        "dns":"",
                                        "port":"10050"
                                }],
                                "groups" : [{"groupid": group_id2}],
                                "templates" : [{"templateid": template_id2}],
                        })
			
