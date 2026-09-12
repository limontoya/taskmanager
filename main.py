from task_manager import TaskManager
def print_menu():
    print("\n --=== Gestor de Tareas Inteligente ===--")
    print("   | 1. Añadir tarea")
    print("   | 2. Listar tareas")
    print("   | 3. Completar tarea")
    print("   | 4. Eliminar tarea")
    print("   | 5. Salir")
    print("    ---------------------------.\n")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Elige una opción: ")) #cast la eleccion a int

            match choice:
                case 1:
                    description = input("Descripción de la tarea: ")
                    manager.add_task(description)

                case 2:
                    manager.list_tasks()

                case 3:
                    id = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id)

                case 4:
                    id = int(input("ID de la tarea a eliminar: "))
                    manager.delete_task(id)

                case 5:
                    print("Saliendo ...")
                    break

                case _: #default
                    print("Opción no válida, selecciona otra...")

        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

if __name__ == "__main__":
    main()