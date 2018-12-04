#!/usr/bin/python

import sys

'''
Reducer para DineroGastadoPorPersona
Realizado por Javier Galvez

Este Reducer tambien puede ejectuar tareas de combiner
ya que la suma de un todo es igual que la suma de las partes
'''

subproblema = None
acumulado = 0

for claveValor in sys.stdin:
    persona, cantidad = claveValor.split("\t", 1)

    cantidad = float(cantidad)

    # El primer subproblema es la primera persona recibida
    if subproblema == None:
        subproblema = persona

    # Si estamos en el mismo subproblema, realizamos la lógica solicitada
    if subproblema == persona:
        if(cantidad >= 3000):
            acumulado = acumulado + 1
    else:
        # La persona ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, acumulado) )

        # Pasamos al siguiente subproblema
        subproblema = persona
        if(cantidad >= 3000):
            acumulado = 1
        else:
            acumulado = 0


# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, acumulado) )