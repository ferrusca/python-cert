# -*- coding: utf-8 -*-

pali1 = 'Edipo lo pide' #length 13
pali2 = 'Somos o no somos' #length 16
pali3 = 'Anita lava la tina' #length 18

def esPalindromo(string):
	return string == string[::-1]

def getPalindromo(string):
	"""
	Funcion que obtiene el palíndromo más extenso en una cadena 
	Args:
		string (str): cadena en la que se va a buscar el palíndromo 
	Returns:
		(str): el palindromo más largo encontrado
	"""
	palindromos = []
	string = string.replace(" ", "").lower()
	for i,char in enumerate(string):
		indices = [ind for ind, a in enumerate(string) if a == char]
		indices = indices[indices.index(i):]
		for j in range(1, len(indices)):
			if(esPalindromo(string[indices[0]: indices[j]+1])):
				palindromos.append(string[indices[0]: indices[j]+1]) 
	if(len(palindromos) > 0):
		palindromos.sort(lambda x,y: cmp(len(x), len(y)))	
	# print(palindromos)
	return palindromos[-1]

print(getPalindromo(pali2+pali3+pali1))
print(getPalindromo("osoanitalavaosolatina"))