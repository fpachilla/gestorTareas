import json

class Tarea:

    contadorTareas = 0

    def __init__ (self, titulo, descripcion, prioridad, estado):
        Tarea.contadorTareas += 1
        self._idTarea = Tarea.contadorTareas
        self._titulo = titulo
        self._descripcion = descripcion
        self._prioridad = prioridad
        self._estado = estado

    def __str__(self):
        return f'ID: {self._idTarea}, titulo: {self._titulo}, descripcion: {self._titulo}, prioridad: {self._prioridad}, estado: {self._estado}'

listaTareas = []
while True:
    seleccion_tarea = input(f'''
    Seleccione la acción requerida:
    
    1-Ingresar nueva tarea
    2-Listar tareas existentes
    3-Marcar tarea como completada
    4-Eliminar tarea
    5-Guardar datos
    
    Holamundo :)
    
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
        archivo = open('tasks.json', 'w', encoding='utf8')

        datos = []

        for tarea in listaTareas:
            datos.append({
                "id": tarea._idTarea,
                "title": tarea._titulo,
                "desc": tarea._descripcion,
                "prioridad": tarea._prioridad,
                "estado": tarea._estado
            })

        with open("tasks.json", "w", encoding="utf8") as archivo:
            json.dump(datos, archivo, indent=4)