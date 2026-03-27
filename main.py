from storage import *
from tareas import Tarea
from gestion_tareas import *

listaTareas = []
cargar_tareas(listaTareas)

while True:
    seleccion_tarea = input(f'''
    Seleccione la acción requerida:
    
    1-Ingresar nueva tarea
    2-Listar tareas existentes
    3-Cambiar estado de la tarea
    4-Eliminar tarea
    5-Guardar datos
    
    ''')

    if seleccion_tarea == "1":
        configurar_tarea(listaTareas)

    elif seleccion_tarea == "2":
        mostrar_tareas(listaTareas)

    elif seleccion_tarea == "3":
        tareaACambiar = int(input(f'Ingrese el ID de tarea a la cual desea cambiar el estado: '))
        cambiar_estado_tarea(listaTareas, tareaACambiar)

    elif seleccion_tarea == "4":

        tareaAEliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
        eliminar_tarea(listaTareas, tareaAEliminar)

    elif seleccion_tarea == "5":

        guardar_tareas(listaTareas)