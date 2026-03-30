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

    def to_dict(self):
        return {
            'idTarea': self._idTarea,
            'titulo': self._titulo,
            'descripcion': self._descripcion,
            'prioridad': self._prioridad,
            'estado': self._estado
        }