# -*- coding: utf-8 -*-
"""

Seminario Python

Lectura1:

Ejemplo de lectura de un archivo de texto. 

@authors: D. G. Reina
"""

# Leemos el fichero linea a linea

fichero = open("song.txt", 'r')

for i, line in enumerate(fichero):
    print line
    numero_lineas = i
 
print "numero de lineas del fichero:", numero_lineas 

#%% Vamos a complicar un poco mas el asunto

for line in fichero:
    palabras = line.split(" ") # separamos las lineas en palabras
    for palabra in palabras:
        print palabra # imprimimos palabra a palabra



