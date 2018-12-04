#!/usr/bin/python

import sys

'''
Mapper de DineroGastadoPorPersona
Realizado por Javier Galvez
'''

# Para cada medida recibida calculamos los pares <persona, cantidad>
for linea in sys.stdin:
    linea = linea.strip()
    persona , cantidad = linea.split("\t")
    print("%s\t%s" % (persona, cantidad))
