#!/usr/bin/python

import sys

'''
Reducer para WordCounter
Realizado por Javier Galvez
'''

subproblema = None
suma = 0

for claveValor in sys.stdin:
    palabra, cantidad = claveValor.split("\t", 1)

    cantidad = int(cantidad)

    #El primer subproblema es la primera palabra recibida,
    if subproblema == None:
        subproblema = palabra
        suma = cantidad

    #Si es el mismo anyo calculamos la temperatura maxima
    if subproblema == palabra:
        suma = suma + cantidad
    else:
        # La palabra ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, suma) )

        # Pasamos al siguiente subproblema
        subproblema = palabra
        suma = cantidad

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, suma) )