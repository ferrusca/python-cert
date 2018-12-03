 # -*- coding: utf-8 -*-

def factorial(n):
	fact = 1
	for i in range(n, 1, -1):
		fact *= i
	return fact

def	esPrimo(n):
	"""
	Funcion que determina si un numero es primo
	Args:
		n (int): el numero a evaluar si es primo
	Returns:
		True si n es primo, falso de otra manera  
	"""
	return (factorial(n-1) + 1) % n == 0   

def regresarLista(size, n=1):
	"""
	Funcion que devuelve una lista de numeros primos
	Args:
		size (int): el numero de elementos que contendrá la lista
		n(int): el numero a evaluar si es primo
	Returns:
		lista con numeros primos
	"""
	# caso base
	if(size == 0): 
		return [n] if esPrimo(n) else []
	# caso general		
	else:
		if(esPrimo(n)):
			return [n] + regresarLista(size-1, n+1) 
		return regresarLista(size, n+1)
		
print(regresarLista(10))