import json

from gestion_tareas import crear_tarea
from tareas import Tarea

def cargar_tareas(lista):
    try:
        with open("tasks.json", "r", encoding="utf8") as archivo:
            contenido = archivo.read().strip()

            if not contenido:
                return []

            data = json.loads(contenido)
            for t in data:
                crear_tarea(lista, t["title"], t["desc"], t["prioridad"], t["estado"])

    except FileNotFoundError:
        return []

def guardar_tareas(lista):

    datos = []

    for tarea in lista:
        datos.append({
            "id": tarea._idTarea,
            "title": tarea._titulo,
            "desc": tarea._descripcion,
            "prioridad": tarea._prioridad,
            "estado": tarea._estado
        })

    with open("tasks.json", "w", encoding="utf8") as archivo:
        json.dump(datos, archivo, indent=4)