#!/usr/bin/python
# coding=utf-8

import sys

'''
Reducer para ErrorEnEstimacionPorCompra
Realizado por Javier Galvez
'''

subproblema = None
diferencia = 0

for claveValor in sys.stdin:
    persona, cantidad = claveValor.split("\t", 1)
    cantidad = int(cantidad)

    # El primer subproblema nos permite hacer la primera definición,
    if subproblema == None:
        subproblema = persona

    # Vamos sumando la diferencia de las cantidades pasadas para cada persona
    if subproblema == persona:
        diferencia = diferencia + cantidad
    else:
        # La persona ha cambiado por lo que hemos finalizado el subproblema
        print("%s\t%s" % (subproblema, abs(diferencia)))

        # Pasamos al siguiente subproblema
        subproblema = persona
        diferencia = cantidad

# el anterior bucle no emite el ultimo resultado
print("%s\t%s" % (subproblema, abs(diferencia)))