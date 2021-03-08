from funciones import *
import sys

fichero = "./proyecto_json/ejercicios_json/partidosfutbol.json"
partidos = leer_json(fichero)


    

opcion=0

while opcion!=6:
    if opcion==1:
        for i in listado_equipos(partidos):
            print(i)
    if opcion==2:
        print(numero_partidos(partidos))
    if opcion==3:
        equipo = input("dime el nombre del equipo que quieres buscar: ")
        liga = input("dime el nombre de la liga ")
        busqueda = busqueda_partido(partidos,equipo,liga)

    if opcion==4:
        liga = input("dime el nombre de la liga ")
        for i in busqueda_liga(partidos,liga):
            print(i)
    if opcion==5:
        equipo = input("dime el nombre del equipo que quieres buscar: ")
        busqueda = busqueda_url_partido(partidos,equipo)
    opcion= menu(opcion)