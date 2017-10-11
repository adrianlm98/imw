## UT1-A3:Trabajo con virtual hosts

### Sitio web 1

http://imw.alu5971.me y http://imw.alu5971.me/mec/

Primero creamos un virtual hosts en sites-available donde indicamos el subdominio imw y dentro del subdominio la carpeta mec. Indicamos la ruta donde se aloja el subdominio.

![img](./img/sitioweb1/sites-available-imw.png)

Enlazamos el archivo que está en sites-available con el de sites-enabled con un enlace simbolico.

![img](./img/sitioweb1/ln-s-imw.png)

Ahora creamos los html que se van a ejecutar en cada pagina (index.html).

##### *Imagen:*

Simplemente hacemos un img src y escribimos la ruta donde tengamos el archivo.

![img](./img/sitioweb1/html-img.png)

Para descargar una imagen desde nuestra máquina de clase (imw) hacia la nube (cloud) utilizamos el comando scp.

![img](./img/sitioweb1/scpimagen.png)

Y movemos hacia la carpeta que hemos creado previamente (la que nosotros queramos) en mi caso en webapps/imw/img.

![img](./img/sitioweb1/mvimagen.png)

##### *PDF:*

Repetimos el proceso creamos un index.html donde pondremos la ruta donde se encuentra el pdf que queremos mostrar(boe.pdf) con el a href="ruta".

![img](./img/sitioweb1/html-pdf.png)

Utilizamos scp para subir nuestro pdf al servidor.

![img](./img/sitioweb1/scppdf.png)

Y lo movemos hacia el directorio correspondiente.

![img](./img/sitioweb1/mvboe.png)

Una vez terminado reiniciamos el servicio nginx.

![img](./img/sitioweb1/reiniciar-servicio.png)

### Resultado final:

##### *Imagen :*

http://imw.alu5971.me

![img](./img/sitioweb1/resultadoimw-img.png)

##### *PDF :*

http://imw.alu5971.me/mec/

![img](./img/sitioweb1/resultadoimw-pdf.png)

### Sitio web 2

http://varlib.alu5971.me:9000

Creamos un virtual host en sites-available llamado varlib.Donde indicamos el subdominio, el puerto de escucha, la carpeta donde se encuentra el contenido a mostrar y autoindex para que se pueda ver.

![img](./img/sitioweb2/available-varlib.png)

Creamos el enlace simbolico del sites-available en sites-enabled.

![img](./img/sitioweb2/ln-s-varlib.png)

Reiniciamos el servicio nginx.

![img](./img/sitioweb2/systemctl-restart-varlib.png)

#### Resultado final

![img](./img/sitioweb2/resultado-varlib.png)

### Sitio web 3

https://ssl.alu5971.me/students/

Primero creamos el virtual host en sites-available llamado ssl. Donde indicamos el puerto de escucha,el subdominio, la ruta donde se encuentra las claves(certificados) para el ssl y el directorio students junto con el archivo de usuario y contraseña(.htpasswd).

![img](./img/sitioweb3/sites-available-auth-basic-ssl.png)

Creamos la carpeta en el directorio webapps.

![img](./img/sitioweb3/mkdir-students.png)

Creamos el index.html dentro de students donde pondremos los nombres de los alumnos.

![img](./img/sitioweb3/index.png)

Ahora creamos la clave encriptada "aula108" con el comando perl.

![img](./img/sitioweb3/perl-ssl.png)

La copiamos y la añadimos al archivo .htpasswd junto con el nombre de usuario "usuario1" (en mi caso puse admin pero fue un error que ya está solucionado) utilizando el echo.

![img](./img/sitioweb3/echo-ssl.png)

Para prohibir el acceso al fichero .htpasswd utilizaremos el location junto con la ruta del archivo que queremos denegar y el deny all.

![img](./img/sitioweb3/prohibir-.htpasswd.png)

Reiniciamos el servicio nginx.

![img](./img/sitioweb3/systemctl-students.png)

### Resultado final

##### *Login*

![img](./img/sitioweb3/prueba1.png)

##### *html*

![img](./img/sitioweb3/prueba2.png)

### Sitio web 4

http://redirect.alu5971.me


Primero creamos los virtual host target y redirect en sites-available.

##### *Target*

Añadimos el nombre del subdominio target.alu5971.me, la carpeta donde se va alojar y la dirección de los logs(hay que crear la carpeta redirect en /var/log/nginx)

![img](./img/sitioweb4/target.png)

##### *Redirect*

Añadimos un virtual host que su subdominio será redirect.alu5971.me, escucha en el puerto 80, añadimos la carpeta donde se encuentra y le decimos que retorna hacia target.alu5971.me.

Añadimos otro virtual host que su subdominio será www.redirect.alu5971.me que escucha en el puerto 80 y retorna hacia target.alu5971.me.

![img](./img/sitioweb4/sites-available-redirect.png)

Creamos las carpetas necesarias con mkdir.

![img](./img/sitioweb4/mkdir-redirect.png)

![img](./img/sitioweb4/mkdir-redirect-var.png)

(una vez accedamos a las páginas se nos crearán los archivos .log)

![img](./img/sitioweb4/log.png)

![img](./img/sitioweb4/mkdir-target.png)



Ahora para añadir la página web al directorio webapps/target necesitamos usar el comando scp

     scp nombredelarchivo alu5971@alu5971.me:

Quedará en nuestro home.
Después instalamos el unzip y lo descomprimimos.

![img](./img/sitioweb4/unzip.png)

Y lo movemos al directorio deseado en este caso webapps/target.

![img](./img/sitioweb4/html.png)

Reiniciamos el servicio nginx.

![img](./img/sitioweb4/restart.png)

### Resultado final

http://www.redirect.alu5971.me/hola/

http://www.redirect.alu5971.me/probando/

http://redirect.alu5971.me/test/

![img](./img/sitioweb4/resultado.png)
