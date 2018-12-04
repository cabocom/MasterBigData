#!/usr/bin/python
# coding=utf-8

import sys

'''
Mapper de DineroGastadoPorPersona
Realizado por Javier Galvez
'''

# Para cada medida recibida calculamos los pares <persona, cantidad>
for linea in sys.stdin:
    linea = linea.strip()
    persona , tienda = linea.split("\t")
    print("%s-%s\t%s" % (persona, tienda, 1))

 
