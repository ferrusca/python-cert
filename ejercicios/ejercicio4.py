#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from poo import Becario
from random import choice

calificacion_alumno = []
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
        calificacion_alumno.append(Becario(b, choice(calificaciones)))

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print alumno, type(alumno)

asigna_calificaciones()
imprime_calificaciones()