# TaskManager

Aplicacion de consola en Python para gestionar tareas desde un menu interactivo. Las tareas se guardan en `tasks.json`, por lo que permanecen disponibles al cerrar y volver a ejecutar el programa. Tambien incluye una opcion de inteligencia artificial para convertir una tarea compleja en entre 3 y 5 subtareas.

## Funcionalidades

- Crear tareas con un identificador numerico autoincremental.
- Listar las tareas guardadas y mostrar si estan completadas.
- Marcar una tarea como completada.
- Eliminar una tarea.
- Generar subtareas a partir de una descripcion compleja mediante OpenAI.
- Cargar y guardar los datos automaticamente en formato JSON.
- Continuar con una lista vacia si el archivo de datos no existe o no es valido.

## Requisitos

- Python 3.10 o posterior, porque el menu utiliza `match`/`case`.
- Dependencias indicadas en `requirements.txt`.
- Una clave de API de OpenAI solo para la funcionalidad de tareas complejas.

## Instalacion

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Si PowerShell impide activar el entorno, puede instalarse la dependencia usando directamente el interprete del entorno:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Configuracion de OpenAI

La aplicacion carga las variables de entorno mediante `python-dotenv`. Crea un archivo `.env` en la raiz del proyecto:

```dotenv
OPENAI_API_KEY=tu_clave_de_openai
```

No subas `.env` ni la clave al repositorio. Si la variable no existe, la opcion de tareas complejas muestra un error y las funciones locales siguen disponibles.

## Ejecucion

```powershell
python main.py
```

El menu ofrece estas opciones:

| Opcion | Accion |
| --- | --- |
| 1 | Anadir una tarea manualmente |
| 2 | Listar las tareas |
| 3 | Completar una tarea por su ID |
| 4 | Eliminar una tarea por su ID |
| 5 | Generar y anadir subtareas con OpenAI |
| 6 | Salir |

Las operaciones de crear, completar y eliminar guardan los cambios inmediatamente. Los IDs no se reutilizan durante la ejecucion: el siguiente ID es el mayor ID existente mas uno.

## Formato de datos

`tasks.json` contiene una lista de objetos. Cada objeto tiene un `id`, una `description` y el indicador booleano `completed`:

```json
[
	{
		"id": 1,
		"description": "Preparar la presentacion",
		"completed": false
	}
]
```

Los registros que no sean objetos o no tengan `id` y `description` se ignoran al cargar. Si el JSON no es valido, el programa inicia una lista vacia y no se detiene.

## Estructura del proyecto

```text
TaskManager/
├── ai_service.py             # Integracion con OpenAI
├── main.py                   # Menu y punto de entrada
├── task_manager.py           # Modelo Task y logica de persistencia
├── tasks.json                # Datos locales de ejemplo
├── requirements.txt          # Dependencias Python
├── tests/
│   └── test_task_manager.py  # Pruebas unitarias
└── README.md                 # Documentacion
```

## Pruebas

Ejecuta las pruebas unitarias desde la raiz:

```powershell
python -m unittest discover -s tests -v
```

Las pruebas cubren la creacion de tareas, la asignacion de IDs, la recuperacion ante JSON invalido, la finalizacion usando IDs de tipo texto y la carga de tareas iniciales en memoria.

## Uso como modulo

Tambien se puede utilizar `TaskManager` desde otro script:

```python
from task_manager import TaskManager

manager = TaskManager("mis_tareas.json")
task = manager.add_task("Revisar documentacion")
manager.complete_task(task.id)
manager.list_tasks()
```

Para pruebas o datos simulados, se puede evitar la lectura del archivo pasando `initial_tasks`:

```python
manager = TaskManager(initial_tasks=[
	{"id": 10, "description": "Tarea simulada", "completed": False}
])
```

## Notas y limitaciones

- La interfaz es interactiva y esta pensada para una ejecucion local.
- No hay usuarios, autenticacion ni sincronizacion remota.
- La opcion de IA depende de la disponibilidad de la API, de una clave valida y de la configuracion del modelo `gpt-5` usada por `ai_service.py`.
- Los errores de red o de la API se convierten en un mensaje generico para el usuario.
- `TaskManager` imprime mensajes de estado directamente en consola, por lo que no es una capa de persistencia silenciosa.

## Apendice: contenido original del README

El siguiente contenido ya formaba parte del README y se conserva como referencia.

### PIP INSTALL CON .VENV

Recordar que si uso un entorno propio en el VSCode, en lugar del `pip install` solo, debo usar el python del `.venv`:

```powershell
.\.venv\Scripts\python.exe -m pip install python-dotenv openai
```

Revisamos instalacion:

```powershell
.\.venv\Scripts\python.exe -m pip show python-dotenv
```

Igual para el `pip freeze`:

```powershell
.\.venv\Scripts\python.exe -m pip freeze > requirements.txt
```

### WINDOWS Y POWERSHELL

Para que mi VSCode no pida en cada commit-push el passphrase, ejecuto, en un PowerShell como administrador:

```powershell
PS C:> Get-Service ssh-agent

Status   Name               DisplayName
------   ----               -----------
Stopped  ssh-agent          OpenSSH Authentication Agent
```

Lo pongo en automatico:

```powershell
PS C:> Set-Service -Name ssh-agent -StartupType Automatic
PS C:> Start-Service ssh-agent
PS C:> Get-Service ssh-agent

Status   Name               DisplayName
------   ----               -----------
Running  ssh-agent          OpenSSH Authentication Agent
```

Agrego el ID de mi SSH:

```powershell
PS C:> ssh-add C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst
Enter passphrase for C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst:
Identity added: C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst (micorreolj@mail.com)
```

Muestro las identidades SSH cargadas:

```powershell
PS C:> ssh-add -l
256 SHA256:1234567890A micorreolj@mail.com (ED25519)
PS C:>
```
