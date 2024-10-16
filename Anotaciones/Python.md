# 3. Cliente-Servidor con Python
Para poder crear nuestro primer servidor, utilizando el estandar [WSGI](https://docs.python.org/es/3/library/wsgiref.html). El cual es una interfaz estándar entre el servidor web y aplicaciones web escritas en Python. Usaremos la función make_server.

> Nota:
> Se creará un entorno virtual y dentro de la carpeta app se encontrarán todos los archivos trabajados.

Dentro de main.py importamos make_server _from wsgiref.simple_server import make_server_
Justo como su nombre lo dice, creamos un servidor sencillo.

## Primer servidor en Python

Después, creamos la función app() la cual será la encargada de responder a cada una de las peticiones por parte del cliente. Esta función debe tener dos parámetros env y start_response. Env es un diccionario con información relevante con respecto a la petición del cliente, dentro del diccionario se encuentra el método del protocolo HTTP, utilizado para crear la petición. 

Por ejemplo, dentro del diccionario seremos capaces de conocer el método del Protocolo HTTP utilizado para crear la petición, además, por supuesto de conocer el encabezado o los encabezados que el usuario que el cliente envíe el agente, el QuerySet, etcétera. Todo lo relacionado con respecto a la petición del cliente.

El parámetro start_response es un [callback](https://www.ionos.mx/digitalguide/paginas-web/desarrollo-web/que-es-un-callback/) el cual recibe de forma obligatoria dos argumentos, el primer argumento no será más que el status code que se le enviará al cliente, y el segundo argumento no será más que un listado de encabezados, los encabezados que el servidor envíe al cliente. Es obligatorio que mandemos llamar esta función callback. Es la respuesta del servidor.

Dentro de la función llamamos al callback y por status code sería '200 OK' ya que es el código para mostar que todo va bien, y como segundo parámetro le pasamos la variable headers o encabezados, la cual es una lista de tuplas. Las tuplas tendrán dos valores, el nombre del encabezado y su valor. Por ejemplo Content type, con este header se le informa al cliente que tipo de respuesta obtendrá, es esta caso texto plano.

Se retorna un valor para el cliente, un mensaje por ahora. El cual debe ser codificado a UTF-8, para hacer esto llamamos al método encode() y le pasamos como argumento el tipo de codificación. Todo esta respuesta dentro de una lista.

Para crear el servidor se almacena en una variable la función importada make_server. Esta función recibe 3 argumentos. 1. la dirección donde se ejecuta el servidor y está a la escucha. 2. El puerto con el que estará a la escucha y 3. La función encargada que responder a las peticiones. En nuestro caso sería localhost, 800 y la app.

Después se ejecuta el método serve_forever() para indicarle al servidor que se encuentre a la escucha por siempre, hasta que nosotros lo detengamos.

## Retornar página HTML
Así como retornamos texto plano también podemos retornar páginas web. 
Para ser prácticos crearemos una constante donde se encontrará el maquetado html. Colocamos un titulo y el mensaje de respuesta lo pasamos en el cuerpo del maquetado. 

Dentro de app modificamos la respuesta del servidor colocando en el return un listado de nuestra constante pero en fomato de bytes, para hacer esto ejecutamos el método bytes(), como primer argumento nuestra constante HTML y como segundo la codificación.

Para finalizar, cambiamos  el segundo elemento de la tupla del encabezado de texto plano a texto html . Lo que se entiende que el tipo de contenido o Content-Type que se retorna como rspuesta del servidor es un texto html.

## Páginas web dinámicas
Mediante la majestuosa librería de jinja2 podremos renderizar plantillas/templates para generar páginas web dinámicas. Dentro de los templates podremos usar variables, ciclos, condicionales, ... 

>Instalación que ocurre dentro del entorno virual.
Para instalar [jinja2](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation) vamos a la web y ejecutamos el comando. _pip install Jinja2_ para Unix.

Creamos la carpeta templates y dentro tendremos index.html. Es este creamos un maquetado sencillo (tecleas el signo ! y pulsas enter.) Con esto podemos eliminar la constante HTML creada en main.py

Haremos de los mensajes que se muestran en index, variables. Usando las dobles llaves para denotarle jinja que eso de ahí es una variable. Este juego de llaves tiene por nombre _placeholder_ y se remplazará por el valor de la variable cuando se renderice el template, obteniendo un sitio web dinámico.

Dentro de main importamos las clases enviroment y FileSystemLoader ambas vienen con jinja2.
Los siguiente es crear una varible que almacenará la ruta exacta donde se almacenen los templates a utilizar. Usando la función Enviroment y com oprimer parámetro se define la ruta de la carpeta templates con la función FileSystemLoader.

En otra variable almacenamos la llamada de los templates, pasamos como argumento el nombre del template a usar.

Para renderizarlo se usa el método render, como el template usa dos variables, le pasamos un diccionario como argumento, en el cual definimos las variables con sus valores. Este render se almacena en una variable que se retorna en formato bytes y codificada.

Aquí se puede hacer una conexión a una base de datos y realizar una consulta con esos datos o bien, consumir una API o leer de un archivo, ...