# 5. Desarrollo API
## Hola mundo

Para crear nuestro servicio web, usaremos FastAPI y Uvicorn como librerías externas, aquí la web.  
En la consola: _pip install "fastapi[standard]"_ y también _pip install uvicorn_

Dentro de app, creamos main.py, importamos la clase FastAPI y la instanciasmos. Con solo esto creamos nuestra aplicación que será nuestro servicio web.  
Para ser más específicos, en los parámetros especificamos el título, descrpción y la versión del proyecto a realizar.  

Para levantar el servidor usamos el comando: _uvicorn main:app --reload_ Es main porque el archivo se llama así y es app porque la instancia de la clase lleva ese nombre. Y con la bandera reload es para reiniciar el server por si ocurre algún cambio.  
Accedemos a la web que nos indica y para este punto nos dará un error "not found" pero este error viene del servidor, el cual está a la escucha.  
Así como en flask, crearemos una ruta usando un decorador. Con flask es app.route y la ruta, pues con fastAPI se usa app.get. Y después definimos la función, con un return de un mensaje.

>Es app.get pero el verbo puede ser cualquiera: app.put, app.post, ...

Con esto le indicamos a fastAPI que en dado caso un cliente realice una petición a la ruta indicada utilizando el método get, entonces la función index será la encargada de retornar una respuesta.

Debemos indicarle a python que esta función debe ejecutarse de forma asíncrona. En caso que ocurran múltiples peticiones al mismo tiempo sobre la misma ruta, están serán resueltas de forma asíncronas.

## Documentación

Al crear nuestra app (o instanciarla) se crea autonmáticamente un apartado de documentación, a la cual podemos acceder realizando una petición a /docs . Vemos el titulo, descripción, versión; las url creadas y el método con el cual se accede a ellas, si se da click en una de ellas, vemos información más especifica, si ocupa parámetros o no, las respuestas: el codigo y la descripción asociada. Si queremos probar el endpoint le damos a _"Try it out"_ para generar una petición con curl y vemos la respuesta del servidor.

Cada cambio en las rutas se verá reflejado en la documentación.

## Eventos

Con los eventos de fastAPI podremos programar acciones que se ejecuatn antes o después de ciertos acontecimientos. Para mostrarlo usaremos los eventos startup y shutdown. Eventos con los cuales programaremos acciones al inicio o al finalizar el servidor.

Creamos las funciones con un mensaje de ejemplo. Y para ejecutarlas para los eventos se decoran con app.on_event y pasamos como argumento el nombre del evento que disparará la función.
> Función que se encuentra en desuso pero para este ejemplo funciona sin problema alguno.

### Implementación de lifespan
El uso de app.on_event está deprecado, entonces en la [documentación de fastAPI](https://fastapi.tiangolo.com/advanced/events/), viene la solución, donde en vez de tener dos funciones con dos decoradores, tendremos que importar asynccontextmanager de la librería contextlib y crear una función con el decorador mencionado, la función en asíncrona, de nombre lifespan y recibe la app. Ahora, todo lo que se encuentre antes de la palabra reservada _yield_ se ejecutará antes de iniciar el servidor y todo lo que se encuentre después se ejecutará antes de terminar la conección. Como último paso en los parámetros de nuestra app, instancia de FastAPI, colocamos que _lifespan=lifespan_ el parámetro esperado de nombre lifespan es nuestra función. Y listo.

## Conexión a base de datos
Se usará el gestor de base de datos MySQL, para conectarnos y manipularla, usaremos un ORM, peewee. Se requiere instalar su librería _pip install peewee_ y para el gestor mysql, instalamos el cliente. _pip install mysqlclient_ . Listooooo.

Debemos autenticarnos con el servidor de la base de datos. Ejecutamos: _sudo mysql -u root_ y dentro del servidor hacemos la sentencia de crear la base de datos: _CREATE DATABASE fastapi _project;_ sin el espacio.Después hacemos: _use fastapi _project;_

> Todas las sentencias SQL finalizan con un punto y coma, además de ir en mayúsculas la mayoría de palabras.

Creamos el archivo database.py. Creamos la coneción a la base de datos. Importamos todo de peewee, e instanciamos la base de datos, com primer argumento se coloca la base de datos con la que vamos a trabajar, el segundo es el usuario, seguido de la contraseña, el host y el puerto, este último es el 3306 por defecto de MySQL.  
Con esto conectamos la aplicación fastapi con el gestor base de datos mysql.

Ahora vamos a nuestro archivo main e importamos la base de datos. Para probar la conexión, modificamos la funciópn lifespan, preguntando el estado de la conexión y conectando o desconectando el servidor cual se el caso.

> Si llega a dar un error para ingresar con el usuario root aunque no tenga contraseña visitar: [este enlace](https://stackoverflow.com/a/69042895/27616392)

## Definir modelos/tablas

Modelos o tablas, serán 3: user, movie, user_review. El objetivo: Un servicio donde los usuarios puedan reseñar peliculas. Dentro de database creamos las clases con esos nombres, para considerarlos modelos, heredan de Model. 

Para user, tiene el nombre, contraseña y la fecha por atributos. El usuario es de tipo CharField y se le indica la longitud máxima, además se le indica que los usuarios deben ser únicos, para la contraseña es casi lo mismo, para la fecha instanciamos de DateTimeField y le especificamos la fecha del momento de creación, como siempre al tratar con fechas, importamos datetime. Sobreescribimos el método built-in: str para que cuando se imprima un objeto user, se obtendrá el nombre. También creamos otra clase, Meta, donde indicamos la base de datos y el nombre de la tabla.

En Movie solo tiene 2 atributos, titulo y fecha de creación, es casi igual a User.

Para UserReview haremos referencia a los dos modelos anteriores con llaves foraneas, como primer parámetro se tiene la clase a la cual se hace referencia y como segundo, una referencia que será un atributo del objeto User con el que podrá acceder a sus reseñas. Los otros dos atributos de la clase son para los reviews, calificaciones y fechas. También se reescribe str (pero imprimimos el nombre del usuario y el titulo de la pelicila) y tiene otra clase model.

En main importamos los modelos Y dentro del livespan antes del yiel creamos las tablas. Si las tablas ya existen, no pasará nada, en caso contrario, se crean. Se reinica el servidor y accedemos a mysql en la terminal y con los comandos: _use (nombredelatabla)_ y _SHOW TABLES;_ veremos nuetros modelos pero ahora en tablas de SQL, para revisar sus atributos hacemos: _DESC (nombredelatabla);_ SQL crea automáticamente la llave primaria.

## Crear usuario

Con el método post insertaremos los usuarios a la base de datos. En main creamos otra ruta. con el método post, la función es asíncrona. Para que el cliente pueda crear un nuevo usuario necesita enviar el nombre y contraseña. 

Con pydantic podremos validar los datos de entrada y salida, procedemos a crear schemas.py, aquí crearemos los modelos que permitan validar los datos. Importamos BaseModel, creamos el modelo de usuario con los atributos obligatorios de usuario y contraseña.

Vamos a main.py e importamos el modelo base en la función que estabamos creando le decimos que reciba como parámetro un objeto user de tipo UserBaseModel, al hacer esto obligamos al cliente a mandar los datos de username y password. el usuario que le pasamos como parámetro será una instancia del modelo/tabla User el cual ejecuta el método create, el cual añade un registro en la tabla que lo mande a llamar, pasandole por argumentos el username y password.

Con esto ya metemos los datos que el cliente pase directamente a la base de datos. Para ver que todo funciona, retornamos el id del usuario ya registrado.

Dentro de la ruta /docs veremos la ruta users, y enviamos los valores de prueba dandole a try it out. Al ejecutar vemos que en cuadro de response body hay un 1, este es el id. También vamos a la base y vemos el usuario creado. _use fastapi project;_ y _SELECT * FROM users_

## Validar username