import json
import sys

def leer_json(fichero):
    with open(fichero) as f:
        datos=json.load(f)
    return datos

def listado_equipos(partido):
    res = []
    
    for i in partido.get("timeline"):
        res.append(i.get("localTeam").get("name"))
        res.append(i.get("visitorTeam").get("name")) 
    return res

def numero_partidos(partidos):
    return len(partidos.get("timeline"))

def busqueda_partido(partidos,equipo,liga):
    for i in partidos.get("timeline"):
        if equipo.upper() == i.get("localTeam").get("name").upper():
            equipo_rival=i.get("visitorTeam").get("name")
            fecha = i.get("startTime")
        if equipo.upper() == i.get("visitorTeam").get("name").upper():
            equipo_rival=i.get("localTeam").get("name")
            fecha = i.get("startTime")
    return print ("Juega contra ",equipo_rival,"a las", fecha)

def busqueda_liga(partidos,liga):
    res =[]
    for i in partidos.get("timeline"):
        if liga.upper() == i.get("championship").get("shortName").upper(): 
            res.append(i.get("localTeam").get("name"))
            res.append(i.get("visitorTeam").get("name"))
    return res

def busqueda_url_partido(partidos,equipo):
    for i in partidos.get("timeline"):
        if equipo.upper() == i.get("localTeam").get("name").upper():
            for a in i.get("sources"):
                url = a.get("url")
        if equipo.upper() == i.get("visitorTeam").get("name").upper():
            for a in i.get("sources"):
                url = a.get("url")  
    return print ("la url es:",url)

def menu(opcion):
    print("")
    print("1- Muestra los nombres de los equipos que participan en las apuestas.")
    print ("2- Muestrame el numero de partidos que hay registradas.")
    print("3- Muestra el nombre del equipo rival y la fecha del partido.")
    print("4- Muestra los nombres que participan en una liga determinada.")
    print("5- Muestra la url de donde fue emitido el partido del equipo elegido")
    print("6- Salir.")
    opcion = int(input("dime la opcion a elegir "))
    return opcion