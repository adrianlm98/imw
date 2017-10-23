# UT1-A4: Sirviendo aplicaciones Php y Python

## Sitio web 1

* http://php.alu5971.me

Primero creamos un **virtual host** llamado *php*.

![img](./img/sitio1/captura1.png)

* Añadimos el nombre del servidor *php.alu5971.me*
* Un **index**, en este caso *index.php* porque la página es en **php**.
* **Root** : La dirección donde se ubica el *index.php* que vamos a mostrar.
* Por ultimo añadimos un location para decirle a *nginx* donde tiene que buscar el programa que va a traducir el código **php** *(php-fpm)*.

Después creamos el enlace simbólico con **ln -s**.

![img](./img/sitio1/enlace_simbolico.png)

![img](./img/sitio1/ls_enlace_simbolico.png)

Subimos el archivo **demo_php.zip** a la máquina **cloud**.

![img](./img/sitio1/subir_archivo.png)

Una vez en la máquina cloud descomprimimos el archivo con *unzip*.

![img](./img/sitio1/descomprimir_archivo.png)

Y movemos la carpeta que hemos descomprimido hacia el directorio *webapps/php*.

![img](./img/sitio1/mover_archivo.png)

Por último recargamos el **servicio nginx**.

![img](./img/sitio1/reload_nginx.png)

### Resultado :

![img](./img/sitio1/resultado.png)




## Sitio web 2

* http://now.alu5971.me

Una vez instalado *python* :

    sudo apt-get install python3.6

Instalamos las librerías para el funcionamiento de *python* :

    sudo apt-get install python3.6-dev

Por último instalamos el compilador de C:

    sudo apt install gcc

Creamos la carpeta **now** en nuesto home.

![img](./img/practica1.png)

Creamos el **entorno virtual** en .virtualenvs(carpeta oculta) llamado now.

![img](./img/practica2.png)

Para entrar en nuestro **entorno virtual** tenemos que hacer lo siguiente :

![img](./img/practica3.png)

### uWSGI

Instalamos *flask* y *uwsgi* dentro de nuestro **entorno virtual** (now), serán los encargados de traducir el código *python* para que nginx pueda mostrarlo correctamente :

![img](./img/practica4.png)

![img](./img/practica5.png)

Ahora nos dirigimos a nuestro al directorio **/home/alu5971/now** y creamos un fichero llamado *main.py* donde estará el codigo que aparecerá en la página.

![img](./img/practica8.png)

Ahora lanzamos el proceso que escuchar-a peticiones :

    uwsgi --socket 0.0.0.0:8080 --protocol=http -w main:app

### Configuración del servidor web

Creamos el fichero de configuración para
**uWSGI** (/home/alu5971/now):


    nano uwsgi.ini

![img](./img/practica9.png)

También creamos el fichero *run.sh* en el mismo directorio.

    nano run.sh

![img](./img/practica10.png)

Le damos permisos para poder ejecutarlo.

![img](./img/practica11.png)

### Nginx

Vamos a crear un **virtual host** para *python*.

    sudo nano /etc/nginx/sites-available/now

![img](./img/practica12.png)

* Nombramos al virtual host *now.alu5971.me*

* Añadimos un location para definir el área de intercambio */tmp/now.sock* y otro para definir una ruta donde pondremos los ficheros estáticos.

Y enlazamos el **virtual host** para habilitarlo en **sites-enabled**

![img](./img/practica13.png)

Recargamos el servicio *nginx*:

![img](./img/practica14.png)

Ahora activamos el *run.sh*:

    ./run.sh

![img](./img/practica15.png)

#### Prueba:

![img](./img/practica16.png)

### Supervisor

Utilizamos supervisor para poder controlar nuestro proceso **(Reiniciarlo, apagarlo, pararlo..)**.

#### Configuración

Añadimos un archivo de configuración para que supervisor pueda gestionar *now*.

![img](./img/practica17.png)

* Especificamos el **programa** que vamos a administrar.

* Elegimos el **usuario** encargado de administrarlo.

* Seleccionamos el archivo que tiene el **script** que vamos a ejecutar.

* Activamos el **autostart** para que se active automáticamente.

* Activamos el **autorestart** para que se reinice si hay algún problema.

* Activamos el **killasgroup** para que mate a los grupos hijos.

* Añadimos la ruta donde se van alojar los archivo de **log** (*now.err.log - now.out.log*).

#### Comandos de comprobación :

![img](./img/practica18.png)

![img](./img/practica19.png)

![img](./img/practica21.png)

![img](./img/practica22.png)

#### Modificaciones :

Editamos el fichero */home/alu5971/now/main.py* para que muestre la hora de **Canarias**.

Instalamos *pytz*(dentro del entorno virtual **now**):

    pip install pytz

Y reiniciamos el proceso :

    supervisorctl restart now



![img](./img/modificacion1.png)

![img](./img/modificacion2.png)
