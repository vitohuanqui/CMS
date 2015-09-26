# Instalación

En este repositorio se tiene una app de prueba para la que se han considerado las siguientes herramientas de desarrollo:
### OS
 Para desarrollar el proyecto se necesitan los siguientes paquetes de desarrollo de Python en distribuciones Ubuntu/Debian.

```sh
$ sudo apt-get install build-essential python-dev python2.7-dev
```
 
### pip
Es el manejador de paquetes de python, el cual nos permitira instalar y manejar las dependencias del proyecto.

```sh
$ sudo apt-get install python-pip
```
### virtualenv
Permite generar ambientes virtuales donde se instalaran las dependencias de nuestros proyectos.

```sh
$ sudo pip install virtualenv
```
Una vez instalado debemos ir al directorio donde deseemos que se instale el proyecto y ejecutar:
```sh
$ virtualenv proyect-env
```
Ingresar al ambiente creado y activarlo:
```sh
$ cd proyect-env
$ source bin/activate
```
### Git
Para el manejo de versiones se utilizara Git con el repositorio en Bitbucket
Instalar Git con el siguiente comando:
```sh
$ sudo apt-get install git
```
Y clonar el proyecto en el ambiente virtual:
```sh
$ git clone https://<mi-usuario>@bitbucket.org/josemvaldiviaromero/flask-test.git
```
### Instalar dependencias
Una vez clonado el proyecto, ingresar al repositorio e instalar las dependecias del proyecto que incluyen:
- Flask (framework web minimalista)
- Flask-SQLAlchemy (extension a flask que permite tener un ORM, para facilitar el acceso a la BD)
- En este ejemplo se utiliza Flask-WTForms para hacer un simple form de Log-in
- Flask-REST-Api: Que nos permite hacer una capa de recursos la cual permitira desarrollar el API para el proyecto
- Flask-Bower: Manejo de dependencias de front-end
Para instalar estas dependecias utilizar:
```sh
$ cd flask-test
$ pip install -r requirements.txt
```
Una vez instaladas las dependencias correr el servidor con:
```sh
$ python run.py
```

