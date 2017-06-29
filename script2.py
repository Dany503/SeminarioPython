# -*- coding: utf-8 -*-
"""

Seminario Python

Script 2
@authors:  D. G. Reina
"""

print "Introduce un numero en el intervalo [0, 10]"
var = raw_input() # esta función sirve para obtener information desde el terminal

if var > 5:
    print "Número mayor que 5"
else:
    print "Numero menor que 5"
    
#%%

print "Introduce un data cualquiera"

var = raw_input()

if type(var) == int:
    print "variale tipo entera"

if type(var) == float:
    print "variable tipo flotante"
    
if type(var) == str:
    print "variable tipo cadena"
else:
    print "No tenemos ni idea del tipo"
    
# ¿Qué esta ocurriendo?
    
