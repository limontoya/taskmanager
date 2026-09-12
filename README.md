Recordar que si uso un entorno propio en el VSCode, en lugar del 
 pip install solo, debo usar el python del .venv:

 ''' .\.venv\Scripts\python.exe -m pip install python-dotenv openai '''

Revisamos instalación:

 ''' .\.venv\Scripts\python.exe -m pip show python-dotenv '''

Igual para el pip freeze:

 ''' .\.venv\Scripts\python.exe -m pip freeze > requirements.txt '''
 