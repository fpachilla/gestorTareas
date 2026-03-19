import json
from tareas import Tarea

def cargar_tareas():
    try:
        with open('tasks.json', 'w', encoding='utf8') as archivo:
            data = json.load(archivo)
            return data

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