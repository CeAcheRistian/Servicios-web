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


Para UserReview haremos referencia a los dos modelos anteriores con llaves foraneas, como primer parámetro se tiene la clase a la cual se hace referencia y como segundo, una referencia que será un atributo del objeto User con el que podrá acceder a sus reseñas. Los otros dos atributos de la clase son para los reviews, calificaciones y fechas. También se reescribe str (pero imprimimos el nombre del usuario y el titulo de la pelicula) y tiene otra clase model.

> Se debe hacer referencia al modelo especifico en las llaves foráneas o tendrás problemas en el futuro.

En main importamos los modelos Y dentro del livespan antes del yiel creamos las tablas. Si las tablas ya existen, no pasará nada, en caso contrario, se crean. Se reinica el servidor y accedemos a mysql en la terminal y con los comandos: _use (nombredelatabla)_ y _SHOW TABLES;_ veremos nuetros modelos pero ahora en tablas de SQL, para revisar sus atributos hacemos: _DESC (nombredelatabla);_ SQL crea automáticamente la llave primaria.

## Crear usuario

Con el método post insertaremos los usuarios a la base de datos. En main creamos otra ruta. con el método post, la función es asíncrona. Para que el cliente pueda crear un nuevo usuario necesita enviar el nombre y contraseña. 

Con pydantic podremos validar los datos de entrada y salida, procedemos a crear schemas.py, aquí crearemos los modelos que permitan validar los datos. Importamos BaseModel, creamos el modelo de usuario con los atributos obligatorios de usuario y contraseña.

Vamos a main.py e importamos el modelo base en la función que estabamos creando le decimos que reciba como parámetro un objeto user de tipo UserRequestModel, al hacer esto obligamos al cliente a mandar los datos de username y password. el usuario que le pasamos como parámetro será una instancia del modelo/tabla User el cual ejecuta el método create, el cual añade un registro en la tabla que lo mande a llamar, pasandole por argumentos el username y password.

Con esto ya metemos los datos que el cliente pase directamente a la base de datos. Para ver que todo funciona, retornamos el id del usuario ya registrado.

Dentro de la ruta /docs veremos la ruta users, y enviamos los valores de prueba dandole a try it out. Al ejecutar vemos que en cuadro de response body hay un 1, este es el id. También vamos a la base y vemos el usuario creado. _use fastapi project;_ y _SELECT * FROM users_

## Validar username

Implementaremos una regla de negocios, no podremos introducir un nuevo usario si la longitud no es la pedida. Para ello volvemos a usar field_validator de pydantic dentro de la clase de schemas. Si mandamos un usuario que no cumpla con la longitud, entonces nos dará el error levantado y el codigo de error 422. 

Acabamos de usar fastAPi y pydantic al mismo tiempo!

## Generar contraseña

Necesitamos encriptar la contraseña para que no sea guardada como texto plano, exiten muchis tipos de hash para hacer esto, acá se usará el MD5. Para crear la contraseña definimos un método de clase en el modelo User, importamos hashlib, almacenamos el resultado de la llamada a md5 y le pasamos la contraseña en texto plano con una codificación. Y retornamos la contraseña encriptada en hexadecimal.

En main, modificamos el método de crear usuarios, instanciamos la respuesta del método de clase recién hecho y ese lo pasamos a la base. Y listo, para verificar agregamos un usuario por medio de la documentación (/docs) y lo verificamos en la base.

## Elementos duplicados

Si queremos añadir un usuario que ya se tiene en la base, dará un error y se morirá el server. Entonces, dentro de la función create_user y antes de generar el hash, realizamos una consulta a la tabla. En la sentencia se pretende obtener algún registro con el nombre del usuario que está pasando el cliente y a esta sentancia le ejecutamos el método exits, el cual nos dará un booleano si se encontró alguna coincidencia. Si es así, retornamos un error al cliente. usando una excepcion que viene con fastAPI con el código de error por parte del cliente y un mensaje.

Con esto mostramos al cliente mejores indicaciones y no se cae el servidor.

## Retornar objetos JSON

En la función create_user retornaremos el usuario y su id como diccionario, estructura que será tomada como un objeto json. PERO, fastAPI recalca que se deben usar modelos para validar los datos de salida, en este caso.

## Objeto Response

Creamos un nuevo modelo para validar los datos de salida, en schema especificamos los datos del usuario y su id e importamos el modelo en main. Donde retornaremos un  objeto del tipo UserResponseModel con los datos obetenidos del usuario. Para finalizar, le indicamos a fastAPI que queremos serializar nuestro objeto (objeto json) para que sea enviado como respuesta del servidor. Para esto, como segundo parámetro del decorador de la ruta le indicamos el modelo que se usará como respuesta. Y listo, obtenemos como respuesta un objeto json pero validando los datos de salida con un modelo.

## Serializar objetos

Que pasa si queremos mandar un objeto de tipo user y no uno serializado, para este proyecto el objeto user es un objeto de tipo model de peewee. Si lo retornarmos directamente, se va a quejar, porque no es un objeto json o un diccionario. Crearemos otra clase en schemas donde transformaremos el objeto a un diccionario, cambiando lo atributos a llaves.

El objeto a retornar será un objeto UserResponse, entonces, el objeto de tipo user que ahora se tiene se convertirá en un objeto del tipo que debe ser, UserReponse. Como cada clase tiene atributos diferentes debemos convertir los atributos definidos a llaves de un diccionario. De esta manera solo compartiremos con el cliente los atributos definidos dentro de schema y no dentro del modelo de peewee, esta información es irrelevante para el usuario.

Esta nueva clase (PeeweeGetterDict) hereda de una clase propia de pydantic para obtener los atributos de los objetos. Dentro sobreescribirá el método get, con las llaves y valores por parámetro. Se obtiene cada uno de los atributos de los instancias de User y se compararán con UserResponse, para obtener los valores de los atributos que coincidan con ambos modelos, el id y username.

Ahora, dentro de la clase UserResponse, crearemos la clase Config, con el atributo orm_mode. FastAPI no implementa ningun ORM, queda a cada quien implementarlo, en este proyecto es peewee, la clase que se acaba de hacer, solo funcionará para el ORM de peewee. Como segundo atributo tenemos getter_dict y este es una asignación de la clase recién hecha.

Con esto ya podemos retornar un objeto del tipo User y el server retornará un diccionario con las características del objeto instancia de UserResponse.

## Crear reseñas 

Creamos un nueva ruta o endpoint para la reseña de peliculas. Se validarán los datos de entrada y de salida, con los valores de entrada crearemos un nuevo objeto y persistirlo en la base de datos. 

Empezamos creando la ruta para las reviews, después cachamos los datos del cliente, así como le hicimos con el usuario, los datos a cachar son el id del usuario, de la peli, la reseña y el score o calificación. Estos datos los cachamos y almacenamos en la base, tendremos que validar, una vez más, los datos de entrada y de salida, con un modelo, esto en schemas.py

La clase ReviewRequest es muy similar a UserRequest, son la manera de cachar los datos de entrada del cliente. Como recordatorio: Todos los atributos definidos dentro del modelo son requeridos, es decir, obligatorios. Ahora, en main importamos la clase y pasamos como argumento en la función correspondiente un objeto user_review qu es del tipo de la clase recién hecha. Con esto ya tenemos los datos de entrada que nos manda el cliente, a partir de ellos, vamos a crear y persistir el objeto.

Dentro de la función, instanciamos a UserReview, clase dentro de database. Y, así como en la función create_user, mapeamos o pareamos las clases de schema y database respectivas a las reviews. Estamos construyendo un objeto del tipo UserReview con datos que cachamos y verificamos del cliente, volvemos persistentes estos datos. Para retornar un objeto user_review con la data obtenida, debemos crear un modelo que pase los datos a un diccionario.

Creamos una clase (ReviewResponseModel) para los datos de salida relevantes para el cliente (sus atributos). También creamos una clase Config identica a la de UserResponse para serializar los datos. En main importamos la clase recién hecha y especificamos en la ruta correspondiente que va a retornar un objeto del mismo tipo.

Con esto validamos los datos de entrada y de salida, y a partir de los datos que pase el cliente creamos y persistimos un objeto.

Para poder reseñar peliculas, deben haber películas en la base de datos, para meter esa información hay dos caminos: 1. Registrar un nuevo endpoint para que el cliente cree peliculas o 2. Crear los registros directamente en la tabla. Es más conveniente meter los datos directamente.

### Registrando los datos por un endpoint.
Agregamos la ruta en main y hacemos casi lo mismo, paso por paso, pero ahora, para movies, creamos modelos para los valores de entrada y de salida, los mapeamos, creamos el objeto instancia de Movies y la data se vuelve persistente. Además, añadí las columnas de director y año tanto en la base de datos, directamente a SQL y cacho esos valores de entrada y de salida.

### Registrar las peliculas directamente en la base de datos.
En una consola entramos a sql especificamos que vamos a usar la base: _use fastpi project_ y con el comando _INSERT INTO movies(campos) VALUES ('valores a añadir')_ añadimos los campos de las peliculas, separados por comas, para la columa de fecha, el valor a añadir es NOW().

### Introduciendo reseñas
Después de haber metido peliculas a la base. Probamos el endpoint en /docs. Es posible agragar y modificar reseñas, solo apuntamos a el id de la pelicula para agregarla o actualizarla.

### Refactorización de la clase Config
Creamos una clase ResponseModel y dentro colocamos lo que ya existía y se repetia de la clase config en todos las clases con apellido ResponseModel. Esta nueva clase la vamos a heredar a todas las clases que respondan al cliente: User, Movie y Review con apellido ResponseModel.

Así evitamos la repetición de código.

## Validar puntaje
Se hará una validación en el score, donde solo se acepte el rango de 1 a 10. Si el cliente no manda un número en este rango, se lanzará un error. Así como en username usamos el decorador field_validator.

## Validar llaves foraneas
Se va a condicionar que el usuario y la pelicula que manda el cliente existan en la base de datos. Con esto evitamos error con llaves foraneas.

En la función create_review obtenemos el primer registro que se tenga de la review por medio del id del usuario, si no lo haya, entonces salta la excepción. Lo mismo para pelicula.

## Listado de reseñas
Haremos un endpoint con todas las reseñas (/reviews). Se hace una petición a la base para obtener todas las reseñas y retornamos unb listado de objetos ReviewResponse.
> Si no permite retornar el objeto tan cual, hacemos un list comprehesion: [user_review for user_review in reviews]

## Obtener reseña
El cliente mandará el id de la reseña y solo se mostrará esa reseña. Esto en una nueva ruta, pero ahora con parámetros que va a mandar el cliente, los parámetros van dentro de _placeholders_ (/reviews/{parametro}), la función debe recibir el mismo parámetro, es requerido. Obtenemos el primer elemento que tenga el mismo id y lo retornamos, sino hay nada, mandamos una excepción.

## Actualizar reseñas
En una ruta con parámetros, pero ahora con el verbo put, porque vamos a actualizar. La función es casi identica a la anterior, almacenamos la coincidencia, sino existe, exepción, si sí, de actualizan los valores, estos valores deben enviarse a través del cuerpo de la petición HTTP, debemos validar los datos de entrada, para esto usaremos un modelo (ReviewRequestPutModel).

Dentro de la clase vienen los atributos necesarios para actualizar la reseña: la reseña misma y el score. También debemos validar que el score esté en un rango, pero anteriormente ya teníamos un field_validator con este código, entonces haremos lo mismo que con la clase config, abstraeremos ese código en una nueva clase y luego se heredara de ella.

La importamos en main y como parámetro de la función la cachamos para que con los valores del cliente se persista en la base. Y actualizamos los valores del user_review con los nuevos de review_request. Para persistir los datos, se usa el método de save y se retorna el objeto actualizado y como siempre, se especifica como segundo parámetro del decorador el tipo de objeto que se retorna.

## Eliminar reseñas
Para eliminar tenemos el método delete. Es casi lo mismo que los métodos anteriores, solo cambia el método a llamar, en este caso es .delete_instace() proveido por peewee

> Para verificar el CRUD nos vamos a docs y a la base.

## Paginacion
En el subtema de listado de reseñas retornamos todas las reseñas existentes, lo cual no es una buena práctica, ya que pued ehaber miles de registros en la base. Vamos a paginar la consulta, el servidor retornará bloques de registros, conforme el cliente lo vaya requiriendo, no sapoyaremos de un __QuerySet__.

QuerySet: El cual es un listado de valores que podemos enviar a través de la url, a diferencia de los parámetros, un queryset es opcional y se conforma por el nombre del valor y su valor. Los queryset se encuentran en la ruta, depués del signo de interrogación.

Implementamos un refactor sobre la función get_reviews. Empezamos agregando el método paginate() al select anterior, con este método se paginará la consulta y recibe 2 parámetros, la referencia a página actual y la cantidad máxima de elementos a mostrar. En los parámetros de la función agregamos estos valores que tienen valores por defecto. Por defecto mostramos la pagina 1 y 10 registros por página.

En docs veremos que hay una casillas para los valores de página y la cantidad de valores. En el cURL vemos la petición y como se manda con el signo de interrogación y la especificación del queryset. (/reviews?page=1&limit=1)

## Modelos relacionados
Al ver las reseñas como respuuesta del servidor, podemos der los id, pero no el nombre de las peliculas, así que relacionaremos modelos para mostrar esta respuesta.

Modificaremos el atributo movie_id del modelo ReviewResponse por movie que es del tipo MovieResponse, con esto ya estaremos relacionando objetos. Una reseña le pertenece a una pelicula y una pelicula tiene sus atributos id, titulo, año y director.

Cada que retornemos un objeto del tipo ReviewResponse en automático se realiza una consulta para poder objetener el objeto relacionado, en este caso, la pelicula. UserReview

## Refactor del proyecto
Hasta este momento __YA TENEMOS UNA API totalmente funcional__ pero, todas las rutas están en un mismo archivo, lo cual no está bien, vamos a modularizar las rutas. Para tener un solo archivo para las rutas respecto a los usuarios, otro donde vayan las rutas de peliculas y otro de reseñas. Obteniendo un proeycto más fácil de leer y mantener.

Dentro de la carpeta app renombramos main como init para convertirlo en un paquete, dejando dentro de la carpeta app solo a database.py y schemas.py.

Ahora, creamos un archivo main FUERA de la carpeta app, e importamos nuestra API de nombre app. Adentro de init debemos cambiar las importaciones, especificamente las que vienen de database y de schema. Como ahora es un paquete debemos agregar un punto a los archivo que están en la misma carpeta/paquete.

>Para levantar el servidor nos posicionamos en la carpeta que contenga el archivo main.

Creamos la carpeta routers dentro de app, con su respectivo init para que sea un paquete y agregamos dos archivos nuevos: reviews, users y movies. Dentro de estos archivos colocamos las rutas bajo un contexto. Entonces pasamos todas las rutas de init a sus archivos correspondientes, estas rutas ocupan modelos-clases-heramientas que importamos anteriormente, pues lo volvemos a hacer.

> Como database y schemas están fuera de los archivos, al importar se colocan dos puntos (..database)

Se necesita la importación del objeto app, para añadir nuevas rutas además de cargar la conexión con la API, pero no podemos importarla, así que usamos la herramienta APIRouter, con la cual podremos registrar nuestras propias rutas, bajo un contexto, agregamos un prefijo que se va usar en todas las rutas de este archivo. Y cambiamos el decorador, en vez de app.route, será router.route y en la ruta que antes teniamos ('/users') lo dejamos en nada ('') porque en el prefijo ya tenemos la palabra users.

Dentro de init del paquete router, importamos el objeto router con un apodo para identificarlo de los otros que vamos a importar. Ahora vamos al init del paquete app e importamos el router, para incluir las rutas creadas e importadas usamos el método de include_router() con un listado de rutas, el cual es llamado por nuestra app.

Hacemos lo mismo pero ahora en movies y reviews.

## Refactor rutas
Para mandar la ruta del prefijo desde init del paquete de app creamos una nueva instancia de apirouter (api_v1) en el cual tendremos el prefijo que todas nuestras rutas comparten, este objeto es ahora quien manda a llamar a include_route con las rutas de reviews,movies y users, para que esto surta efecto debe ser nuestra app quien mande a llamar a include_router del objeto api_v1 el cual, a su vez ya incluye las rutas.

En los modulos de las rutas debemos borrar la parte del prefijo que se está repitiendo ('/api/v1/') dejando solo la ruta corresdiente.

> Es importante que se especifique la versión por eso se repite tanto el v1.

## Login
Crearemos una ruta para autenticar los usuarios. Con esto podremos saber las reseñas del usuario logeado. En _users.py_ creamos la ruta. Debemos validar los datos de entrada y de salida. Para obtener los datos del usuario que se manda al servidor usamos la clase __HTTPBasicCredential__ de fastAPI  objeto que cacharemos como parámetro de nuestra función. Los objetos de esa clase poden dos atributos, username y password.

Importamos la clase del submodulo security de fastAPI y dentro de la función realizamos una consulta para obtener el usuario comparando lo que nos manda el cliente con lo que tenemos en la base sino existe, excepción, si sí, comparamos las contraseñas, pero la contraseña que se encuentra en la base está encriptada así que tenemos que comparar esa contraseña con la contraseña que nos manda el cliente pero la pasamos por el método de clase que creamos para crear contraseñas encriptadas. Si todo va bien, retornamos el objeto user.

## Cookies
Extenderemos la respuesta al cliente, manteniendo una respuesta stateless, es decir, que ningún dato sensible se almacena.  Se creará y enviará una cookie al cliente, notificando que se logeo.

Para crear una cookie en fastAPI existe un objeto del tipo response, se importa y se coloca un objeto de su tipo como segundo parámetro de la función login. Con este objeto añadiremos una cookie a la respuesta del servidor con su método _set-cookie_ y los parámetros son el id del usuario logeado, pero pueden ser cualquier dato.

## Listado de reseñas v2
Listado de reseñas de un usuario autenticado. Para lograr eso leeremos los valores de cookies. Dentro de user, agregamos la nueva ruta. fastAPI tiene un objeto Cookie el cual recibiremos por parámetro, este objeto tendrá las llevaes-valor que retornemos de la función login. El nombre del parámetro debe ser el mismo que el de la llave. Este parámetro es un entero si se pasa un valor, sino es None.

Obtenemos el usuario por medio de una consulta y retornamos el atributo review del objeto instancia de User, este atributo es una llave foránea. Y le indicamos al decorador que retornaremos una lista de objetos del tipo ReviewResponse.

> Y listo con esto se termina la parte de fastAPI