from tareas import Tarea

def eliminar_tarea(lista, id):

    tareaencontrada = False
    try:
        for tarea in lista:
            if tarea._idTarea == id:
                lista.remove(tarea)
                tareaencontrada = True
                print("Tarea eliminada.")
                break

        if not tareaencontrada:
            print("No se encontró el ID ingresado")

    except ValueError:
        print("Debe ingresar un numero entero")

def agregar_tarea(lista):

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
        estado_tarea = input(
            f'Solamente se puede ingresar "pendiente" o "hecha". Por favor ingrese una de esas opciones: ')
    tareaIngresada = Tarea(titulo_tarea, descripcion_tarea, prioridad_tarea, estado_tarea)

    lista.append(tareaIngresada)

def mostrar_tareas(lista):
    for tarea in lista:
        if tarea._estado == "pendiente":
            estado_mostrable = " "
        else:
            estado_mostrable = "X"
        print(f'''[{estado_mostrable}] ({tarea._idTarea}) {tarea._titulo} - Prioridad: {tarea._prioridad}''')

def cambiar_estado_tarea(lista, id):

    tareaencontrada = False
    try:
        for tarea in lista:
            if tarea._idTarea == id:
                if tarea._estado == "pendiente":
                    tarea._estado = "hecha"
                else:
                    tarea._estado = "pendiente"
                tareaencontrada = True
                print("Se cambió el estado de la tarea.")
                break

        if not tareaencontrada:
            print("No se encontró el ID ingresado")

    except ValueError:
        print("Debe ingresar un numero entero")