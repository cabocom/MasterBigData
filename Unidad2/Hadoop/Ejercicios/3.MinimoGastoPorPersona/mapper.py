#!/usr/bin/python
# coding=utf-8

import sys

'''
Mapper de MinimoGastoPorPersona
Realizado por Javier Galvez
'''

# Para cada registro recibido emitimos los pares <persona, cantidad>
for linea in sys.stdin:
    linea = linea.strip()
    persona , cantidad = linea.split("\t")
    print("%s\t%s" % (persona, cantidad))
