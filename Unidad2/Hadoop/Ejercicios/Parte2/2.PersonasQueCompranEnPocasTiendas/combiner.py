#!/usr/bin/python
# coding=utf-8

import sys

'''
Reducer para MaxTemp
Realizado por Javier Galvez
'''

subproblema = None
suma = 0

for claveValor in sys.stdin:
    palabra, cantidad = claveValor.split("\t", 1)

    #El primer subproblema es la primera palabra recibida,
    if subproblema == None:
        subproblema = palabra

    # La palabra ha cambiado por lo que hemos finalizado el subproblema
    if subproblema != palabra:  
        persona, tienda = subproblema.split("-", 1)      
        print("%s\t%s" % (persona, tienda) )

        # Pasamos al siguiente subproblema
        subproblema = palabra

# el anterior bucle no emite el ultimo resultado
persona, tienda = subproblema.split("-", 1) 
print("%s\t%s" % (persona, tienda) )