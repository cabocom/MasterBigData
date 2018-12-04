#!/usr/bin/python

import sys

'''
Reducer para MaxTemp
Realizado por Javier Galvez
'''

subproblema = None
tempMaxima = None

for claveValor in sys.stdin:
    anyo, temp = claveValor.split("\t", 1)

    #Convertimos temperatura a float
    temp = float(temp)

    #El primer subproblema es el primer anyo recibido,
    if subproblema == None:
        subproblema = anyo
        tempMaxima = temp

    #Si es el mismo anyo calculamos la temperatura maxima
    if subproblema == anyo:
        if temp > tempMaxima:
            tempMaxima = temp
    else:
        # El anyo ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, tempMaxima) )

        # Pasamos al siguiente subproblema
        subproblema = anyo
        tempMaxima = temp

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, tempMaxima) )