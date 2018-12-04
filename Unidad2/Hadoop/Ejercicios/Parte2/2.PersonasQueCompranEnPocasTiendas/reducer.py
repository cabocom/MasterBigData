#!/usr/bin/python
# coding=utf-8

import sys

'''
Reducer para PersonasQueCompranEnPocasTiendas
Realizado por Javier Galvez
'''

subproblema = None
acumulado = 0

for claveValor in sys.stdin:
    persona, tienda = claveValor.split("\t", 1)

    # El primer conjunto nos permite hacer la primera definición,
    if subproblema == None:
        subproblema = persona

    # Vamos sumando el número de tiendas diferentes en las que ha estado la persona
    if subproblema == persona:
        acumulado = acumulado + 1
    else:
        # La palabra ha cambiado por lo que hemos finalizado el subproblema
        if(acumulado <= 3):
            print(subproblema)

        # Pasamos al siguiente subproblema
        subproblema = persona
        acumulado = 1

# el anterior bucle no emite el ultimo resultado
if(acumulado < 3):
    print(subproblema)