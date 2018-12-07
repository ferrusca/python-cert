 # -*- coding: utf-8 -*-
import random 
seeder = 'qwertyuiopasdfghjklzxcvbnm1234567890+]{,.-/!#$%&_(*)=?QWERTYUIOPASDFGHJKLZXCVBNM'
pwdLength = 8
numbers = ['0','1','2','3','4','5','6','7','8','9']
specialChar = ['!',']','{',',','.','-','/','!','#', '$', '%', '&', '_', '(', '*', ')', '=', '?']
upper = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

def securePassword(char, string=''):
	"""
	Funcion que devuelve una contraseña con requerimientos
	Args:
		char (str): caracter que se insertará en la contraseña
		string (str): contraseña que se tiene hasta el momento
	Returns:
		string (str): una contraseña que tiene al menos 1 MAYUSCULA, 1 CARACTER ESPECIAL y 1 NUMERO
	"""
	if(len(string) == pwdLength):
		for s in string:
			if(s in specialChar):
				for s in string:
					if(s in numbers):
						for s in string:
							if(s in upper):
								return string
	if(len(string) == pwdLength):
		index = random.choice([0,1,2,3,4,5,6,7])
		#reemplazo en una posicion ALEATORIA un caracter para que se cumplan los requisitos de la contraseña
		return securePassword(random.choice(seeder), string[:index] + char + string[index+1:])
	else:
		return securePassword(random.choice(seeder), string+char)

print(securePassword(random.choice(seeder), random.choice(seeder)))