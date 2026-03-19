from storage import *
from tareas import Tarea

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
        titulo_tarea = input(f'Ingrese el titulo de la tarea: ')
        descripcion_tarea = input(f'Ingrese la descripcion de la tarea: ')
        while True:
            try:
                prioridad_tarea = int(input("Ingrese prioridad (1-3): "))

                if 1 <= prioridad_tarea <= 3:
                    break
                else:
                    print("La prioridad debe estar entre 1 y 3.")

            except ValueError:
                print("Debe ingresar un número entero.")
        estado_tarea = input(f'Ingrese la estado de la tarea (solo puede ser "pendiente" o "hecha"): ')
        while (estado_tarea != "pendiente" and estado_tarea != "hecha"):
            estado_tarea = input(f'Solamente se puede ingresar "pendiente" o "hecha". Por favor ingrese una de esas opciones: ')
        tareaIngresada = Tarea(titulo_tarea, descripcion_tarea, prioridad_tarea, estado_tarea)

        listaTareas.append(tareaIngresada)

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

        try:
            tareaAEliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
            encontrada = False
            for tarea in listaTareas:

                if tarea._idTarea == tareaAEliminar:
                    listaTareas.remove(tarea)
                    encontrada = True
                    print("Tarea eliminada.")
                    break

            if not encontrada:
                print("No existe una tarea con ese ID.")

        except ValueError:
            print("Debe ingresar un número entero.")

    elif seleccion_tarea == "5":

        guardar_tareas(listaTareas)