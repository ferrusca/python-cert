# -*- coding: utf-8 -*-
#UNAM-CERT

import sys
import csv
import xml.etree.ElementTree as ET
from datetime import datetime   

file = 'nmap.xml'
fwrite = 'results.csv'

def getHostState(file, state):
    list = [['ip', 'estatus', 'dominio']]
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            s = host.find('status').get('state')
            if(s == state):
                nombre = ''
                hostnames = host.find('hostnames')
                if(hostnames != None):
                    for hostname in hostnames.findall('hostname'):
                        if hostname.get('name'):
                            nombre = hostname.get('name') 
                addr = host.find('address').get('addr')
                list.append([addr, s, nombre])
        return list

def getPortOpen(file, portNumber):
    list = [['ip', 'puerto', 'estatus' 'dominio']]
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            p = host.find('ports')
            if (p != None):
                for pid in p.findall('port'):
                    if (pid.get('portid') == portNumber and pid.find('state').get('state') == 'open'):
                        addr = host.find('address').get('addr')
                        nombre = ''
                        hostnames = host.find('hostnames')
                        if(hostnames != None):
                            for hostname in hostnames.findall('hostname'):
                                if hostname.get('name'):
                                    nombre = hostname.get('name')
                        list.append([addr, pid.get('portid'), pid.find('state').get('state'), nombre])          
        return list

def getServerType(file, serverName):
    list = [['ip', 'Tipo de servidor', 'dominio']]
    nombre = ''
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if (ports != None):
                for port in ports.findall('port'):
                    addr = host.find('address').get('addr')
                    for service in port.findall('service'):
                        if(service.get('product') and serverName in service.get('product').lower()):
                            hostnames = host.find('hostnames')
                            if(hostnames != None):
                                for hostname in hostnames.findall('hostname'):
                                    if hostname.get('name'):
                                        nombre = hostname.get('name')
                            list.append([addr, service.get('product'), nombre])
        return list

def writeCsv(file, fwrite):
    with open(fwrite, 'wb') as f:
        writer = csv.writer(f)
        f.write('Host apagados')
        f.write('\n')
        writer.writerows(getHostState(file, 'down'))
        f.write('\n')
        f.write('Host prendidos')
        f.write('\n')
        writer.writerows(getHostState(file, 'up'))
        f.write('\n')
        f.write('Host con puerto 22 abierto')
        f.write('\n')
        writer.writerows(getPortOpen(file, '22'))
        f.write('\n')
        f.write('Honeypots')
        writer.writerows(getServerType(file, 'dionaea'))
        f.write('\n')

writeCsv(file, fwrite)