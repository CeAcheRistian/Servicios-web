# cURL
## Introducción a cURL
cURL es una herramienta para poder testear nuestros servicios web, específicamente las APIs. Es una herramienta de líneas de comandos integrada para los s.o basados en Unix. Con esta herramienta se puede transferir información para diferentes protocolos de internet.

Para realizar las peticiones sin mucho problema iremos a [https://httpbin.org/](httpbin.org). Sitio web que permite realizar peticiones HTTP, mediante los principales verbos del protocolo.

Verificamos que se esté instalado curl con el comando: _curl --version_. En caso que se encuentre un windows vaya a [curl.se](https://curl.se/download.html) y descarga la versión de windows

Lo siguiente a hacer es una petición get, obteniendo un recurso por parte del servidor, en este caso httpbin.org. 

Ejecutamos _curl https://httpbin.org/get_
Se le conoce como endpoint al ultimo tramo de la url, en este caso es get/.

Se nos retorna un objeto JSON, confirmando que la petición se realizó de forma exitosa. Puesto que el servidor retorna una respuesta exitosa. En el objeto JSON se tiene como atributos los argumentos, encabezados, el origen y la url.

## Envío de parámetos
Para envíar valores al servidor, nos apoyaremos en los [QuerySet](https://tutorial.djangogirls.org/es/django_orm/). Un QuerySet es, en esencia, una lista de objetos de un modelo determinado. Un QuerySet te permite leer los datos de la base de datos, filtrarlos y ordenarlos.

Para mandar valores al servidor colocamos entre comillas dobles la url de curl en el comando curl y al finalizarla url colocamos un signo de interrogación, así se le indica al servidor, que a partir de aquí inicia el QuerySet. i.e los parámetros con sus correspondientes valores. Ejemplo:

_curl "https://httpbin.org/get?name=Christian"_

En el atributo args del objeto JSON retornado, encontramos el parámetro y su valor mandados. 

Podemos pasar n cantidad de valores al QuerySet, solo tenemos que separarlos con un ampersand (&)

_curl "https://httpbin.org/get?name=Christian&edad=27"_

## Encabezados
Con la bandera _-H_ seguido de comillas dobles y dentro se definen los encabezados. Por ejemplo un accept: application/json le indica el servidor que el cliente puede aceptar un objeto json como respuesta. Al ejecutar, en el atributo encabezados vemos lo añadido.

_curl "https://httpbin.org/get?name=Christian&edad=27" -H "accept: application/json"_

Se coloca la bandera -H por cada encabezado a agregar.

Para conocer todos los encabezados por parte de la respuesta como cliente, utilizamos la badnera _-i_