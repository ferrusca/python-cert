# -*- coding: utf-8 -*-
#UNAM-CERT
# Obtener un DICCIONARIO por comprensión que devuelva como llave los numeros odiosos menores a 50 y... 
# ...como valor una tupla con su valor binario y hexadecimal.
# Un número odioso es aquel que tiene numero impar de unos en su representación binaria
print({x:(bin(x), hex(x)) for x in range(50) if bin(x).count('1') % 2 != 0})