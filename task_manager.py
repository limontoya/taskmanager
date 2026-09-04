class Task:

    #Inicializador
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    #Sobreescribo metodo _str_
    def __str__(self):
        status = "OK" if self.completed else " " #ternaria de python
        return f"[{status}] #{self.id}: {self.description}"


#logica principal del programa
class TaskManager:

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea creada: {description}")

    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                return
        print(f"Tarea no encontrada: #{id}")

    def delete_task(self):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")
    