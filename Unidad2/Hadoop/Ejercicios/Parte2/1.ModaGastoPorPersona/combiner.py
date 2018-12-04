#!/usr/bin/python

import sys

'''
Reducer para MaxTemp
Realizado por Javier Galvez
'''

subproblema = None
acumulado = 0

for claveValor in sys.stdin:
    conjunto, trash = claveValor.split("\t", 1)

    #El primer subproblema es la primera palabra recibida,
    if subproblema == None:
        subproblema = conjunto        

    #Si es el mismo anyo calculamos la temperatura maxima
    if subproblema == conjunto:
        acumulado = acumulado + 1
    else:
        # La palabra ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, acumulado) )

        # Pasamos al siguiente subproblema
        subproblema = conjunto
        acumulado = 1

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, acumulado) )