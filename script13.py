# -*- coding: utf-8 -*-
"""

Seminario Python

Script 13

Importamos un módulo que hemos creado nosotros

@authors: D. G. Reina
"""

import funciones_matematicas

print "Ejemplo de suma de dos números"
print funciones_matematicas.funcion_suma(1,2)

#%%
from funciones_matematicas import funcion_multiplicacion
print funcion_multiplicacion(2, 3)
