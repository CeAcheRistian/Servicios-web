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
