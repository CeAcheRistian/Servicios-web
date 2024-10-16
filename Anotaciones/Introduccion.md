# 1. Curso para crear servicios web con Python y FastAPI.
## ¿Qué es HTTP?
Hyper Text Transfer Protocol o en español, Protocolo de transferencias de hipertexto.
Es un protocolo de comunicación con el cual podremos enviar y recibir información. Todos los sitios web usan HTTP, se comunican con el navegador que se usa para visualizar los contenidos. El navegador realiza una **petición** al servidor de la web y el servidor responde con diferentes la página web. El maquetado del sitio web, las hojas de estilo, los arhcivos JavaScript, las imagenes, videos ,... todo fue envíado a través de HTTP.

La S de HHTTPS hace referencia a Secure, es otro protocolo para el envío de información a través de internet, pero de forma segura. Ya no se envían los datos en texto plano, sino con una conexión segura por medio de la encriptación.

Estos protocolos no almecenan ningún tipo de estado después de que la comunicación terminó entre el cliente y el servidor. A esto se le llama **Stateless**. Toda la información relacionada con la conexión y los participantes se pierde, por eso mismo, los servidores tratan a todas sus peticiones como una nueva petición. Para poder almacenar información, se requieren de mecanismos externos tanto del cliente como del servidor. Como lo es la autenticación a un sitio web, solo es necesario ingresar los datos requeridos una vez para navegar en la web.

Las estrategis más habituales de guardar información entre un cliente y un servidor son las cookies y sesiones. Las **cookies** son archivos que el cliente crea y almacena para guardar información acerca de la navegación. Las **sesiones** son valores que se almacenan en el servidor para conservar información entre una petición y otra. Esto permite una cierta memoria entre el cliente y servidor mejorando la experiencia del usuario.

### Métodos del protocolo
Tanto HTTP y HTTPS utilizan método o **verbos** para una correcta comunicación entre el cliente y el servidor. El uso correcto de estos métodos indica de forma implicita que acción debe realizar el servidor y que es lo que necesita el cliente.
Resumen de algunos:
- #### GET
Con este método o veerbo nos permite obtener un recurso por parte del servidor, una página web, una imagen, un video , ... 
- #### POST
Permite crear recursos del servidor, ya sea desde una sesión pasando por nuevos registros en la base de datos hasta nuevos archivos. Como el envío de un login para autenticarnos, esta petición de mandar datos y que se verifiquen, se hace con un método POST, si quisieramos alojar una imagen en el servidor, sería de la misma manera.
- #### PUT
Con el método put actualziamos un recurso del servidor, ya sea actualizar en registro de la base de datos o modificar un archivo ya existente.
- #### DELETE
Eliminamos un recurso en el servidor.

- Estos son los más usados, pero hay muchos más.

Estos verbos hacen referencia a una acción, similares a CRUD: Create, Read, Update, Delete. Algo que se debe aclarar es que estos métodos no modifican el comportamiento del servidor, se definen por el cliente al realizar la petición, pero será el servidor quien realice la acción o no. 
El uso correcto de los métodos del protocolo definen las acciones que el servidor puede usar, todo de forma implícita.

## Arquitectura cliente servidor

### Servidor
Empecemos definiendo qué es un servidor. Dispositivo electrónico capaz de conectarse a una red con un sotfware especial, el cual puede recibir, procesar y responder peticiones. Practicamente cualquier dispositivo electrónico con acceso a internet puede ser un servidor.
Los servidores son creados para centralizar información y que esta se encuentre almacenada en un solo lugar, facilitando su recuperación y procesamiento de la misma. AL tener la información en un solo lugar, podemos tener un mayor control sobre ella, ya que solo hay una entidad que gestiona los recursos. En los servidores se pued almacenar cualquier tipo de información.
Dependiendo del servicio que preste el servidor se le llama de diferentes formas: Servidor web, de correos, de almacenamiento, ...

### Cliente
Un cliente es una pieza de software capaz de realizar peticiones a un servidor; entidad que requiere un servicio de un servidor. Se denomina petición o **request** a la acción de solicitar alguin tipo de recurso al servidor.
Los navegadores como Firefox o Chrome son ejemplos de clientes. Se encargan de realizar múltiples peticiones a múltiples servidores. También pueden obtener y procesar las respuestas del servidor para mostrarnos la página web.
Se le denomina respuesta o **response** a la información que el sevidor envía para satisfacer una petición.

### Arquitectura cliente-servidor
Arquitectura de software donde participan dos entidades: clientes y servidores. Quienes realizan la petición y quieres la resuelven, esta arquitectura y el protocolo HTTP(S) es la forma de interactuar a través de internet. Un cliente puede realizar múltiples peticiones a múltiples servidores y un servidor tiene la obligación de responder múltiples peticiones para múltiples clientes.
El cliente establece la conexión con el servidor, realiza la petición y el servidor se encuentra obligado a enviar una respuesta al cliente, es responsabilidad del cliente obtener y procesar dicha información obtenida.

## Status code
Ya sea, el protocolo HTTP o HTTPS existen diferentes estatus para notificar el estado de una petición. Estos estatus se representan mediante un valor numérico, y a cada uno de estos valores se les conocen como status code, o código de estatus por su traducción al español.
Estos códigos abarcan un rango de números enteros, que comprenden del 100 al 599.Y podemos agruparlos en 5 categorías:
1. Respuestas informativas (100–199),
2. Respuestas satisfactorias (200–299),
3. Redirecciones (300–399),
4. Errores de los clientes (400–499),
5. Errores de los servidores (500–599).

**Respuestas informativas**. Este grupo abarcan del rango 100 al 199. Y cualquier valor que se rse encuentre en este rango hará referencia a un status informativo.
- Por ejemplo, si el cliente recibe como status Code 100, esto le indica que hasta ahora todo va bien, y debe continuar con la solicitud al servidor.
- Otro ejemplo pudiera ser el código 102, que le indica al cliente que el servidor ha recibido la petición y aún se encuentra procesándola..

**Respuestas satisfactorias**. Como su nombre nos indican, serán códigos que le indiquen al cliente que la petición se realizo de forma exitosa, y que no ha ocurrido ningún tipo de error.Este grupo abarca del rango, 200 al 299.Algunos ejemplos son:
- El código 200, que le indica al cliente que la petición y respuesta han sido un éxito.
- El código 201, inducida que la reacción de un nuevo recurso fue exitosa.

**Redirecciones**. Abarca del rango 300 al 399, y cualquier número que se encuentre dentro de este rango indica que hubo algún tipo de redireccionamiento al momento de completar la petición.
- Por ejemplo. El código 301 le indica al cliente que el recurso que ha solicitado ha sido cambiado, ya no se encuentra en la ruta indicada, y por lo tanto no fue posible encontrarlo.
- El código 302 indica que el recurso solicitado ha sido cambiado de forma temporal, por el momento no se encuentra disponible pero lo hará en un futuro.

**Errores de cliente**. Este grupo fue diseñado para poder hacerle saber al cliente que la petición no puede ser completada por que existe un error por parte de él.Este grupo abarca del rango 400 al 499.Algunos ejemplos son los siguientes:
- Error 400 Bad request, Esta respuesta significa que el servidor no pudo interpretar la petición por una sintaxis invalida.
- Error 401 Unathorize. Es necesario autenticarse para que el servidor pueda dar una respuesta satisfactoria al cliente.
- Error 403 Forbide. El cliente no posee los permisos necesarios para completar la operación

**Errores del servidor**. Grupo de códigos que comprenden del número 500 al 599. Este grupo como su nombre lo indica le permiten conocer al cliente que ha habido un error por parte del servidor, y la operación, la petición no puede ser completada.Algunos ejemplos son lo siguientes:
- Error 500: Internal server error: El servidor ha tenido un error y bno sabe como manejarlo.
- Error 503: Service Unavailabl: Ser vidro no esta listo para responder a una peticón. Una causa muy comun de este error pude deberse a que el servidor este caido por mantenimiento o está sobre cargado. 

Es importante, si bien no conocer todos los códigos al pie de la letra, por lo menos si tener en mente los 5 grupos, ya que a partir de ellos sabremos exactamente que responder por cada petición de un cliente, y de esta forma estaremos creando servicios web que sigan con el standares y protocolos previamente definidos.

## REST
Un servicio web se define como un sistema de software designado para soportar la interacción interoperativa de máquina a máquina a través de una red. O más sencillo, un conjunto de protocolos y estándares para el intercambio de información entre aplicaciones, facilitando el acceso a recursos de forma remota.
REST o Representational State Transfer es un ESTILO  de Arquitectura a la hora de realizar una comunicación entre cliente y servidor.
Utilizando la arquitectura REST trabajaremos con los métodos get, post, put, delete. Con REST estos verbos se centran en un recurso en particular, mediante la url.
Utilizando la combinación recurso-métodos es posible tener para un mismo recurso, 6 direcciones url, en escencia, pueden ser más. Ejemplo de ello:

Método | URL | Acción
- GET | /libros | Retona un listado de libros
- POST | /libros | Crea un listado de libros
- GET | /libros{id} | Retorna el libro seleccionado
- PUT | /libros{id} | Actualiza el libro seleccionado
- PATCH | /libros{id} | Actualiza el libro seleccionado
- DELETE | /libros{id} | Elimina el libro seleccionado

Al hacer aplicaciones web RESTful, En este curso API RESTful, se usan protocoloes y estánderes abiertos, lo cual permite escalar nuestra app de forma sencilla. Además de formar una rápida absorción por parte de los usuarios y de los clientes.

[Definición de API, REST y RESTful](https://aws.amazon.com/es/what-is/restful-api/)

