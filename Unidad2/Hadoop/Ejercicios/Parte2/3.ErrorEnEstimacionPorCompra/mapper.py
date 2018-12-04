#!/usr/bin/python
# coding=utf-8

import sys

'''
Mapper de DineroGastadoPorPersona
Realizado por Javier Galvez
'''

# Para cada medida recibida calculamos los pares <persona, cantidad>
for linea in sys.stdin:
    linea = linea.strip()
    persona, datos = linea.split("\t", 1)

    datos = datos.strip()
    accion, cantidad = datos.split(":", 1)

    cantidad = int(cantidad)
    accion = accion.strip()
    if(accion == "gastado"):
        cantidad = -cantidad
    
    print("%s\t%s" % (persona, cantidad))

 
