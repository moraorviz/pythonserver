Servidor python
==================================

Gestor de paquetes pip + python3
----------------------
Framework flask. Se sigue la estructura estandar de
un proyecto flask: plantillas, factorías de aplicaciones, etc.

Necesita la instancia de mongodb en local en el puerto por
defecto. Hace peticiones al otro componente (apiclient) 

La parte importante está en el módulo group (los datos
en el modelo y la lógica en el controler)

Se ejecuta como una aplicación normal de flask
P. ej en unix:
$ export FLASK_APP=main.py
$ flask run

Endpoints que expone:
```
GET "http://127.0.0.1:5000:/group/near?lat=0&lon=0"
GET "http://127.0.0.1:5000:/group/near?lat=-13.4&lon=20.2"
GET "http://127.0.0.1:5000/group/topCities?date=20180507

```
Notas: El caso de uso /near funciona bien (probado hasta num=20000). Devuelve
un array ordenado con el id del grupo mas las coordenadas (con el offset).
El caso de uso /topCities no funciona bien. Falta mayor control sobre
los operadores de reactor para obtener los datos de un día concreto.
Pendiente orquestar los servicios (python ---> jvm)

