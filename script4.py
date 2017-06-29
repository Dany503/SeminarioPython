# -*- coding: utf-8 -*-
"""

Seminario Python

Script 4

Este script sirve de introducción a los bucles while en Python
y otros sentencias útiles para bucles en general

@author: D. G. Reina
"""
#%%
i = 0
while i < 4:
    print i
    i = i + 1 

#%%

for i in range(0,4):
    if i == 2:
        continue
    else:
        print i

#%%

for i in range(0,4):
    if i == 2:
        break
    else:
        print i

#%%

for letter in "Python": 
   if letter == 'h':
      pass
      print "sentencia pass"
   print "Letra actual :", letter # otra forma de imprimir en Python

print "Se acabo!"
