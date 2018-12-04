#!/usr/bin/python
# coding=utf-8

import sys

'''
Reducer para MinimoGastoPorPersona
Realizado por Javier Galvez

Este Reducer tambien puede ejectuar tareas de combiner
ya que el mínimos de un todo es igual que el mínimo de
los mínimos de las partes
'''

subproblema = None
minimo = float(999999)

for claveValor in sys.stdin:
    persona, cantidad = claveValor.split("\t", 1)

    cantidad = float(cantidad)

    # El primer subproblema es la primera persona recibida
    if subproblema == None:
        subproblema = persona

    # Si estamos en el mismo subproblema, calculamos el mínimo
    if subproblema == persona:
        if(cantidad < minimo):
            minimo = cantidad
    else:
        # La persona ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, minimo) )

        # Pasamos al siguiente subproblema
        subproblema = persona
        minimo = cantidad

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, minimo) )