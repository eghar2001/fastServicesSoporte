# fastServicesSoporte
Projecto fastServices para materia Soporte a la gestion de datos con programacion visual.



Pasos para correr el programa
1. Crear entorno virtual dentro de pyCHarm
2. Correr comando $ pip install -r requirements.txt
3. En MySql crean un schema que se llame "fast_services_soporte"
3. Crear archivo dentro de la carpeta inicial del proyecto ("fastServicesSoporte") que se llame .env
4. Dentro de ese archivo, escribir lo siguiente "FAST_SERVICES_SOPORTE = [la connection string la bbdd que crearon]" 
    LOS CORCHETES NO SE INCLUYEN, LO REEMPLAZAN
5. Crean variable de entorno FLASK_APP y le asignan como valor donde este ubicado el archivo
    run.py (para crear una variable de entorno, depende del SO que tengan)
6. corren comando $ flask db upgrade

