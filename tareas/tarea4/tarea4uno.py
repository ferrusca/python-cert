# -*- coding: utf-8 -*-
#UNAM-CERT

import sys
import datetime
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime   

file = 'nmap.xml'
fwrite = 'results.txt'

def md5(file):
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha(file):
    sha1 = hashlib.sha1()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha1.update(chunk)
    return sha1.hexdigest()    

def getHostState(file, state):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            s = host.find('status').get('state')
            if(s == state):
                n += 1
        return str(n)        

def getPortOpen(file, portNumber):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            p = host.find('ports')
            if (p != None):
                for pid in p.findall('port'):
                    # print pid.get('portid'), '-->', type(pid.get('portid'))
                    if (pid.get('portid') == portNumber and pid.find('state').get('state') == 'open'):
                        n += 1
        return str(n)

def getDomainName(file):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            hostnames = host.find('hostnames')
            if (hostnames != None):
                for hostname in hostnames.findall('hostname'):
                    if (hostname.get('name')):
                        n += 1
        return str(n)

def getHttpServer(file):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if (ports != None):
                for port in ports.findall('port'):
                    for service in port.findall('service'):
                        if(service.get('name') == 'http'):
                            n += 1
        return str(n)    

def getServerType(file, serverName):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if (ports != None):
                for port in ports.findall('port'):
                    for service in port.findall('service'):
                        if(service.get('product') and serverName in service.get('product').lower()):
                            n += 1
        return str(n)    

def getOtherServices(file, server1, server2, server3):
    n = 0
    with open(file, 'r') as file:
        root = ET.fromstring(file.read())
        for host in root.findall('host'):
            ports = host.find('ports')
            if (ports != None):
                for port in ports.findall('port'):
                    for service in port.findall('service'):
                        if(service.get('product') and (service.get('name') == 'http' or service.get('name') == 'https')):
                            if(
                                server1 not in service.get('product').lower()
                                and server2 not in service.get('product').lower()
                                and server3 not in service.get('product').lower()
                            ):
                                # print service.get('product')
                                n += 1
        return str(n)

def printStats():
    print 'Hora de ejecución:', now 
    print 'MD5 de archivo xml:', md5
    print 'SHA1 de archivo xml:', sha
    print 'Cantidad de hosts prendidos:', up
    print 'Cantidad de hosts apagados:', down
    print 'Cantidad de hosts con puerto 22 abierto:', p22
    print 'Cantidad de hosts con puerto 53 abierto:', p53
    print 'Cantidad de hosts con puerto 80 abierto:', p80
    print 'Cantidad de hosts con puerto 443 abierto:', p443
    print 'Cantidad de hosts que tienen nombre de dominio:', domain
    print 'Servidores HTTP usados:', http
    print 'Cuántos usan Apache:', apache
    print 'Cuántos honeypots (Dionaea):', honey
    print 'Cuántos usan Nginx:', nginx
    print 'Cuántos usan otros servicios:', other

def writeStats():
    with open(fwrite, 'w+') as file:
        file.write('Hora de ejecución: ' + now)
        file.write('\nMD5 de archivo xml: ' + md5)
        file.write('\nSHA1 de archivo xml: ' + sha)
        file.write('\nCantidad de hosts prendidos: ' + up)
        file.write('\nCantidad de hosts apagados: ' + down)
        file.write('\nCantidad de hosts con puerto 22 abierto: ' + p22)
        file.write('\nCantidad de hosts con puerto 53 abierto: ' + p53)
        file.write('\nCantidad de hosts con puerto 80 abierto: ' + p80)
        file.write('\nCantidad de hosts con puerto 443 abierto: ' + p443)
        file.write('\nCantidad de hosts que tienen nombre de dominio: ' + domain)
        file.write('\nServidores HTTP usados: ' + http)
        file.write('\nCuántos usan Apache: ' + apache)
        file.write('\nCuántos honeypots (Dionaea) :' + honey)
        file.write('\nCuántos usan Nginx: ' + nginx)
        file.write('\nCuántos usan otros servicios: ' + other)
        file.close()

now = str(datetime.now())
md5 = md5(file)
sha = sha(file)
up = getHostState(file, 'up')
down = getHostState(file, 'down')
p22 = getPortOpen(file, '22')
p53 = getPortOpen(file, '53')
p80 = getPortOpen(file, '80')
p443 = getPortOpen(file, '443')
domain = getDomainName(file)
http = getHttpServer(file)
apache = getServerType(file, 'apache')
honey = getServerType(file, 'dionaea')
nginx = getServerType(file, 'nginx')
other = getOtherServices(file, 'apache', 'nginx', 'dionaea')


printStats()
writeStats()
