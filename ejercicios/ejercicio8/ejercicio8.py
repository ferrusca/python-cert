# Expresion regular para determinar si en un archivo hay ip's correctas
# Expresion regular para determinar si en un archivo hay correos electronicos correctos
import sys
import re

expr = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
expr2 = '([0-9a-z]+)+[^@]+@[^.@]+\.[^.@]+'

with open(sys.argv[1]) as file1, open(sys.argv[2]) as file2:
	print "\nIPs"
	for ip in file1.readlines():
		if (re.search(expr, ip)):
			print "coincide"
		else:
			print "no coincide"
	print '\nCorreos'	
	for mail in file2.readlines():
		if (re.search(expr2, mail)):
			print "coincide"
		else:
			print "no coincide"