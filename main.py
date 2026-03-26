from storage import *
from tareas import Tarea
from gestion_tareas import *

listaTareas = []
while True:
    seleccion_tarea = input(f'''
    Seleccione la acción requerida:
    
    1-Ingresar nueva tarea
    2-Listar tareas existentes
    3-Marcar tarea como completada
    4-Eliminar tarea
    5-Guardar datos
    
    ''')

    if seleccion_tarea == "1":
        agregar_tarea(listaTareas)

    elif seleccion_tarea == "2":
        for tarea in listaTareas:
            if tarea._estado == "pendiente":
                estado_mostrable = " "
            else:
                estado_mostrable = "X"
            print(f'''[{estado_mostrable}] ({tarea._idTarea}) {tarea._titulo} - Prioridad: {tarea._prioridad}''')

    elif seleccion_tarea == "3":
        tareaACambiar = int(input(f'Ingrese el ID de tarea a la cual desea cambiar el estado: ')) - 1
        if listaTareas[tareaACambiar]._estado == " ":
            listaTareas[tareaACambiar]._estado = "X"
        else:
            listaTareas[tareaACambiar]._estado = " "


    elif seleccion_tarea == "4":

        tareaAEliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
        eliminar_tarea(listaTareas, tareaAEliminar)

    elif seleccion_tarea == "5":

        guardar_tareas(listaTareas)