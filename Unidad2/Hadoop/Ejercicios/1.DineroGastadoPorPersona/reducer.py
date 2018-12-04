#!/usr/bin/python

import sys

'''
Reducer para DineroGastadoPorPersona
Realizado por Javier Galvez

Este Reducer tambien puede ejectuar tareas de combiner
ya que la suma de un todo es igual que la suma de las partes
'''

subproblema = None
suma = 0

for claveValor in sys.stdin:
    persona, cantidad = claveValor.split("\t", 1)

    cantidad = float(cantidad)

    #El primer subproblema es la primera palabra recibida,
    if subproblema == None:
        subproblema = persona

    #Si es el mismo anyo calculamos la temperatura maxima
    if subproblema == persona:
        suma = suma + cantidad
    else:
        # La palabra ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, suma) )

        # Pasamos al siguiente subproblema
        subproblema = persona
        suma = cantidad

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, suma) )