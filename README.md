<h1>cadastro-csv-zabbix</h1>
<p>Script to register multiple hosts in zabbix .csv file</p>

<h3>Installation</h3>
<pre>
<b>Clone project</b>
git clone https://github.com/viniciustbitencourt/cadastro-csv-zabbix.git

<b>Install dependencies</b>
pip install zabbix_api
python version 2.7.11(lastet)
</pre>

<h3>Configuration</h3>
<pre>Configuration - <b>conf.ini</b>

<b>Zabbix Configuration</b>
<i>[zabbix01]</i>
hostname = hostname of the first server zabbix
user = username of the server
passwd = password of the server

<i>[zabbix02]</i>
hostname = hostname of the second server zabbix
user = username of the server
passwd = password of the server

<i>[relatorio]</i>
csv = .csv file

</pre>
