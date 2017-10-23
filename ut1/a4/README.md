# UT1-A4: Sirviendo aplicaciones Php y Python

## Sitio web 1

* http://php.alu5971.me

* Mostrar la aplicación demo_php

## Sitio web 2

* http://now.alu5971.me

Una vez instalado python :

    sudo apt-get install python3.6

Instalamos las librerías para el funcionamiento de python :

    sudo apt-get install python3.6-dev

Por último instalamos el compilador de C:

    sudo apt install gcc

Creamos la carpeta now en nuesto home.

![img](./img/practica1.png)

Creamos el entorno virtual en .virtualenvs(carpeta oculta) llamado now.

![img](./img/practica2.png)

Para entrar en nuestro entorno virtual tenemos que hacer lo siguiente :

![img](./img/practica3.png)

### uWSGI

Instalamos flask y uwsgi dentro de nuestro entorno virtual (now) :

![img](./img/practica4.png)

![img](./img/practica5.png)

Ahora nos dirigimos a nuestro al directorio /home/alu5971/now y creamos un fichero llamado main.py donde estará el codigo que aparecerá en la página.

![img](./img/practica8.png)

Ahora lanzamos el proceso que escuchar-a peticiones :

    uwsgi --socket 0.0.0.0:8080 --protocol=http -w main:app

### Configuración del servidor web

Creamos el fichero de configuración para
uWSGI (/home/alu5971/now):


    nano uwsgi.ini

![img](./img/practica9.png)

También creamos el fichero run.sh en el mismo directorio.

    nano run.sh

![img](./img/practica10.png)

Le damos permisos para poder ejecutarlo.

![img](./img/practica11.png)

### Nginx

Vamos a crear un virtual host para python.

sudo nano /etc/nginx/sites-available/now

![img](./img/practica12.png)

Y enlazamos el virtual host para habilitarlo en sites-enabled

![img](./img/practica13.png)

Recargamos el servicio nginx:

![img](./img/practica14.png)

Ahora activamos el run.sh:

    ./run.sh

![img](./img/practica15.png)
