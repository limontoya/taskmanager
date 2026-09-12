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

    def __init__(self, filename=None, initial_tasks=None):
        self.filename = filename or self.FILENAME
        self._tasks = []
        self._next_id = 1

        if initial_tasks is not None:
            self._tasks = [Task(int(item['id']), str(item['description']), bool(item.get('completed', False))) for item in initial_tasks]
            self._next_id = max((task.id for task in self._tasks), default=0) + 1
            return

        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea creada: {description}")
        self.save_tasks()  # Guardar tareas después de añadir una nueva
        return task

    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        task_id = int(id)
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return task
        print(f"Tarea no encontrada: #{id}")
        return None

    def delete_task(self, id):
        task_id = int(id)
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return task
        print(f"Tarea no encontrada: #{id}")
        return None

    def load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                if not isinstance(tasks_data, list):
                    raise ValueError("El archivo de tareas no tiene un formato válido.")

                self._tasks = []
                for item in tasks_data:
                    if not isinstance(item, dict):
                        continue

                    task_id = item.get('id')
                    description = item.get('description')
                    completed = item.get('completed', False)

                    if task_id is None or description is None:
                        continue

                    self._tasks.append(Task(int(task_id), str(description), bool(completed)))

                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1
                else:
                    self._next_id = 1
                print(f"Tareas cargadas desde {self.filename}")
        except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError, OSError):
            self._tasks = []
            self._next_id = 1
            print(f"No se pudo cargar {self.filename}. Se iniciará con una lista vacía de tareas.")

    def save_tasks(self, filename=None):
        target = filename or self.filename
        try:
            with open(target, 'w', encoding='utf-8') as file:
                json.dump([task.__dict__ for task in self._tasks], file, indent=4)
            print(f"Tareas guardadas en {target}")
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")
