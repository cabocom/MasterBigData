#!/usr/bin/python

import sys

'''
Mapper de MaxTemp
Realizado por Javier Galvez
'''

# Para cada medida recibida calculamos los pares <anyo, temperatura>
for linea in sys.stdin:
    linea = linea.strip()
    palabras = linea.split(" ")
    for palabra in palabras:
        print("%s\t%s" % (palabra, 1) )
