from storage import *
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
        opcion_filtro = input(f'''
        ¿Deseas colocar algún filtro adicional?:

        1-No, quiero ver todas las tareas
        2-Ver solo tareas pendientes
        3-Ver solo tareas completadas
        4-Ver solo las más prioritarias
                      
        ''')
        if opcion_filtro == "1":
            mostrar_tareas(listaTareas)

        elif opcion_filtro == "2":
            mostrar_tareas_por_estado(listaTareas, "pendiente")

        elif opcion_filtro == "3":
            mostrar_tareas_por_estado(listaTareas, "hecha")

        elif opcion_filtro == "4":
            print("trabajando...")

    elif seleccion_tarea == "3":
        tareaACambiar = int(input(f'Ingrese el ID de tarea a la cual desea cambiar el estado: '))
        cambiar_estado_tarea(listaTareas, tareaACambiar)

    elif seleccion_tarea == "4":

        tareaAEliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
        eliminar_tarea(listaTareas, tareaAEliminar)

    elif seleccion_tarea == "5":

        guardar_tareas(listaTareas)