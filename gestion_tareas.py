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