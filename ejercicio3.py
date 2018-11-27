#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Juan Manual',
            'Ignacio',
            'Valeria',
            'Luis Antonio',
            'Pedro Alejandro',
            'Diana Guadalupe',
            'Jorge Luis',
            'Jesika',
            'JesÃºs Enrique',
            'Rafael Alejandro',
            'Servando Miguel',
            'Ricardo Omar',
            'Laura Patricia',
            'IsaÃ­as Abraham',
            'Oscar']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def aprobadoReprobado():
    r,aprobado = [], [] 
    for a in calificacion_alumno:
        if(calificacion_alumno.get(a) >= 8):
            aprobado.append(a)
        else:
            r.append(a)
    return tuple(aprobado), tuple(r)

def promedio():
    x = 0
    for a in calificacion_alumno:
        x += calificacion_alumno.get(a)
    return float(x)/len((calificacion_alumno))

def conjunto():
    return set(calificacion_alumno.values())

asigna_calificaciones()
imprime_calificaciones()
print(aprobadoReprobado())

print(conjunto())
print("el promedio es ", promedio())