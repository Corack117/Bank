# Hipoo
Prueba Técnica

## Instrucciones de Instalación

### En la raíz de la carpeta del proyecto

`pip install -r requirements.txt `

### Configuración de la base de datos (POSTGRESQL)

* Nombre de la base de datos: `hipoo_db`
* Nombre del usuario/rol: `hipoo_us`
* Contraseña del usuario/rol: `123456`
* HOST: `localhost`
* Puerto: `5432`

## Instrucciones de Ejecución

+ Realizar solo en la primer ejecución.
  + `py manage.py makemigrations`
  + `py manage.py migrate`

`py manage.py runserver
`

## Para ejecutar pruebas unitaras

`pytest`

## Para ejecutar pruebas unitaras desglosadas

`pytest -s`
