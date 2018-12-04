#!/usr/bin/python

import sys

'''
Mapper de NumComprasConGastosAltosPorPersona
Realizado por Javier Galvez
'''

# Para cada entrada recibida emitimos el par <persona, cantidad>
for linea in sys.stdin:
    linea = linea.strip()
    persona , cantidad = linea.split("\t")
    
    print("%s\t%s" % (persona, cantidad))
