import json
import sys

def leer_json(fichero):
    with open(fichero) as f:
        datos=json.load(f)
    return datos

def listado_partidos(partido):
    res = []
    
    for i in partido.get("timeline"):
        lista = []
        lista.append(i.get("localTeam").get("name"))
        lista.append(i.get("visitorTeam").get("name"))
        res.append(lista) 
    return res