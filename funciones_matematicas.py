# -*- coding: utf-8 -*-
"""

Seminario Python

Funciones_matematicas: Módulo de ejemplo de funciones matemáticas

@authors: D. G. Reina
"""

def funcion_suma(a,b):
    suma = a + b
    return suma

def funcion_resta(a,b):
    resta = a - b
    return resta

def funcion_multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

def funcion_division(a,b):
    if b != 0:
        return float(a)/float(b)
    else:
        print "división por cero"

