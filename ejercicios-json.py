from funciones import leer_json, listado_partidos
import sys

fichero = "./proyecto_json/ejercicios_json/partidosfutbol.json"
partidos = leer_json(fichero)

for i in listado_partidos(partidos):
    print(i)
    