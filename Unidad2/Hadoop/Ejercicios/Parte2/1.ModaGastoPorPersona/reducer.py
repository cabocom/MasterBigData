#!/usr/bin/python

import sys

'''
Reducer para DineroGastadoPorPersona
Realizado por Javier Galvez

Este Reducer tambien puede ejectuar tareas de combiner
ya que la suma de un todo es igual que la suma de las partes
'''

subproblema = None
maxRepeticiones = 0
maxCantidad = 0

for claveValor in sys.stdin:
    conjunto, repeticiones = claveValor.split("\t", 1)
    persona, cantidad = conjunto.split("-", 1);

    cantidad = int(cantidad)

    #El primer subproblema es la primera persona recibida,
    if subproblema == None:
        subproblema = persona

    #Si es la misma persona estudiamos el mayor valor repetido
    if subproblema == persona:
        if(repeticiones > maxRepeticiones):
            maxRepeticiones = repeticiones
            maxCantidad = cantidad
    else:
        # La persona ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, maxCantidad) )

        # Pasamos al siguiente subproblema
        subproblema = persona
        maxRepeticiones = repeticiones
        maxCantidad = cantidad

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, maxCantidad) )