# Curso para crear servicios web con Python y FastAPI.
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
-Respuestas informativas (100–199),
-Respuestas satisfactorias (200–299),
-Redirecciones (300–399),
-Errores de los clientes (400–499),
-Errores de los servidores (500–599).
