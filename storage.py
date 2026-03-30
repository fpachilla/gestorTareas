import json
from tareas import Tarea

def cargar_tareas(lista):
    try:
        with open("tasks.json", "r", encoding="utf8") as archivo:
            contenido = archivo.read().strip()

            if not contenido:
                return []

            data = json.loads(contenido) # Carga el contenido del archivo en data, como diccionario
            for t in data:
                tareaCreada = Tarea(
                    t["titulo"],
                    t["descripcion"],
                    t["prioridad"],
                    t["estado"],
                    t["fecha"])
                lista.append(tareaCreada)

    except FileNotFoundError:
        return []

def guardar_tareas(lista):
    with open("tasks.json", "w", encoding="utf8") as archivo:
        json.dump(
            [tarea.to_dict() for tarea in lista], # Convierte las tareas a diccionario para guardarlas en el JSON
            archivo,
            indent=4,
            ensure_ascii=False
        )