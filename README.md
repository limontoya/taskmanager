## PIP INSTALL CON .VENV
Recordar que si uso un entorno propio en el VSCode, en lugar del 
 pip install solo, debo usar el python del .venv:

 ``` .\.venv\Scripts\python.exe -m pip install python-dotenv openai ```

Revisamos instalación:

 ``` .\.venv\Scripts\python.exe -m pip show python-dotenv ```

Igual para el pip freeze:

 ``` .\.venv\Scripts\python.exe -m pip freeze > requirements.txt ```
 
## WINDOWS Y POWERSHELL
Para que mi VSCode no pida en cada commit-push el passprhase, 
 ejecuto, en un powershell como Admin:

 ```
PS C:> Get-Service ssh-agent

Status   Name               DisplayName
------   ----               -----------
Stopped  ssh-agent          OpenSSH Authentication Agent
 ```

Lo pongo en automático:
 ```
PS C:> Set-Service -Name ssh-agent -StartupType Automatic
PS C:> Start-Service ssh-agent
PS C:> Get-Service ssh-agent

Status   Name               DisplayName
------   ----               -----------
Running  ssh-agent          OpenSSH Authentication Agent
 ```

Agrego el id de mi ssh:
 ```
PS C:> ssh-add C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst
Enter passphrase for C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst:
Identity added: C:\mi_ruta_al_ssh\.ssh\id_ed25519_tst (micorreolj@mail.com)
 ```

Me muestra mi ssh:
 ```
PS C:> ssh-add -l
256 SHA256:1234567890A micorreolj@mail.com (ED25519)
PS C:>
 ```
