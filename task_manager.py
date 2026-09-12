import json

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

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea creada: {description}")
        self.save_tasks()  # Guardar tareas después de añadir una nueva

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
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as file:
                tasks_data = json.load(file)
                # self._tasks = [Task(**data) for data in tasks_data]
                self._tasks = [Task(item['id'], item['description'], item['completed']) for item in tasks_data]
                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1
                else:
                    self._next_id = 1
                print(f"Tareas cargadas desde {self.FILENAME}")
        except FileNotFoundError:
            print(f"No se encontró el archivo {self.FILENAME}. Se iniciará con una lista vacía de tareas.")

    def save_tasks(self, filename=FILENAME):
        try:
            with open(filename, 'w') as file:
                #json.dump(["id": task.id, "description": task.description, "completed": task.completed for task in self._tasks], file, indent=4)
                json.dump([task.__dict__ for task in self._tasks], file, indent=4)
            print(f"Tareas guardadas en {filename}")
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")
