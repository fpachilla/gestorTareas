from tareas import Tarea
from datetime import datetime

def eliminar_tarea(lista):

    tareaencontrada = False
    while True:

        try:
            tareaAEliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
            for tarea in lista:
                if tarea._idTarea == tareaAEliminar:
                    lista.remove(tarea)
                    tareaencontrada = True
                    print("Tarea eliminada.")
                    break

            if tareaencontrada == True:
                break

            if not tareaencontrada:
                print("No se encontró el ID ingresado")

        except ValueError:
            print("Debe ingresar un numero entero")

def configurar_tarea(lista):

    while True:
        try:
            titulo_tarea = input(f'Ingrese el titulo de la tarea: ')

            if titulo_tarea.isnumeric():
                print("El titulo de la tarea no puede ser un número")
            elif len(titulo_tarea.strip()) == 0:                 # El metodo strip se usa para eliminar espacios al inicio y final del texto
                print("El titulo de la tarea no puede estar vacío")
            else:
                break

        except ValueError:
            print("Debe ingresar un título válido")

    while True:
        try:
            descripcion_tarea = input(f'Ingrese la descripcion de la tarea: ')

            if descripcion_tarea.isnumeric():
                print("La descripción de la tarea no puede ser un número")
            elif len(
                    descripcion_tarea.strip()) == 0:  # El metodo strip se usa para eliminar espacios al inicio y final del texto
                print("La descripción de la tarea no puede estar vacío")
            else:
                break

        except ValueError:
            print("Debe ingresar una descripción válida")

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
        estado_tarea = input(
            f'Solamente se puede ingresar "pendiente" o "hecha". Por favor ingrese una de esas opciones: ')

    crear_tarea(lista, titulo_tarea, descripcion_tarea, prioridad_tarea, estado_tarea, 0)

def crear_tarea(lista, titulo, descripcion, prioridad, estado, fecha):

    if fecha == 0:
        fecha = datetime.now().strftime("%d/%m/%Y")
    tareaIngresada = Tarea(titulo, descripcion, prioridad, estado, fecha)
    lista.append(tareaIngresada)

def mostrar_tareas(lista):
    for tarea in lista:
        if tarea._estado == "pendiente":
            estado_mostrable = " "
        else:
            estado_mostrable = "X"
        print(f'''[{estado_mostrable}] ({tarea._idTarea}) {tarea._titulo} - Prioridad: {tarea._prioridad} - Fecha: {tarea._fecha}''')

def mostrar_tareas_por_estado(lista, estado):
    for tarea in lista:
        if tarea._estado == "pendiente":
            estado_mostrable = " "
        else:
            estado_mostrable = "X"

        if tarea._estado == estado:
            print(f'''[{estado_mostrable}] ({tarea._idTarea}) {tarea._titulo} - Prioridad: {tarea._prioridad} - Fecha: {tarea._fecha}''')

def mostrar_tareas_prioritarias(lista):
    for tarea in lista:
        if tarea._estado == "pendiente":
            estado_mostrable = " "
        else:
            estado_mostrable = "X"

        if tarea._prioridad == 1:
            print(f'''[{estado_mostrable}] ({tarea._idTarea}) {tarea._titulo} - Prioridad: {tarea._prioridad} - Fecha: {tarea._fecha}''')

def cambiar_estado_tarea(lista):

    tareaencontrada = False

    while True:
        try:
            tareaACambiar = int(input(f'Ingrese el ID de tarea a la cual desea cambiar el estado: '))
            for tarea in lista:
                if tarea._idTarea == tareaACambiar:
                    if tarea._estado == "pendiente":
                        tarea._estado = "hecha"
                    else:
                        tarea._estado = "pendiente"
                    tareaencontrada = True
                    print("Se cambió el estado de la tarea.")

            if tareaencontrada == True:
                break

            if not tareaencontrada:
                print("No se encontró el ID ingresado")

        except ValueError:
            print("Debe ingresar un numero entero")