#!/usr/bin/python

import sys

'''
Mapper de MaxTemp
Realizado por Javier Galvez
'''

# Para cada medida recibida calculamos los pares <anyo, temperatura>
for linea in sys.stdin:
    linea = linea.strip()
    anyo , mes , temp = linea.split("-", 2)
    print("%s\t%s" % (anyo, temp) )
