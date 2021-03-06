# -*- coding: utf-8 -*-
"""

Seminario Python

Escritura1: 

Ejemplo de lectura/escritura de un archivo de texto  

@authors: D. G. Reina
"""

import random

fichero_lectura = open("song.txt", 'r') # abrimos el fichero en modo lectura
fichero_escritura = open("song_modified.txt", 'w')


for line in fichero_lectura:
    palabras = line.split(" ")
    ind = int(random.uniform(0, len(palabras)))
    fichero_escritura.write(palabras[ind])
    fichero_escritura.write('\n')

fichero_escritura.close() # cerramos el fichero, importante para terminar de escribir

# ¿Qué hemos hecho con el orden?
