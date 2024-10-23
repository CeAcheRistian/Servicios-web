# Cliente
## Librería Request
La librer;ia request nos permite realizar nuestras propias peticiones HTTP, vamos a testear nuestro servicio web, consumiremos cada uno de los endpoints registrados.

Se instala con _pip install requests_

Creamos un archivo client.py el cual se encargará de las peticiones. Importamos la librería y almacenamos la URL del endpoint a testear. Para hacer la petición hacemos uso del método get de la librería request y como parámetro la url. Este método nos retornará un objeto de tipo response el cual ahce referencia a la respuesta del servidor, imprimimos el objeto en consola. Lo que obtenemos es un statuc code.

El objeto response, al almacenar la respuesta de get(), puede llamar al método status code., Si la respuesta por parte del servidor es exitosa imprimimos un mensaje de exito. Con el método content almacenamos el contenido de la respuesta, se retorna un objeto de tipo bytes donde se muestra el contenido de la url.

## Encabezados
Podemos almacenar los encabezados en un diccionario. Con el encabezado accept le indicamos al servidor que el cliente acepta como respuesta objetos tipo json, añadimos el encabezado a la petición como segundo parámetro del método get. Para conocer los encabezados en la respuesta del servidor usamos el atributo headers del objeto response.
Podemos convertir la respuesta del servidor en un objeto json, para python es un diccionario. Condicionamos sobre el header content-type y si este retorna un objeto tipo json entonces usamos el método json() el cual transformará al respuesta en un diccionario. Obtenemos la misma respuesta, pero ahora no es un objeto de tipo bytes, sino un listado de diccionarios. Y podemos iterarlo para acceder a las llaves y valores del diccionario.

## Envío de parámetros
Con queryset podremos mandar valores. Una forma es modificar directamente la url, agregamos el signo de interrogación y enviamos los datos, como puede ser la paginación. La segunda forma es con diccionarios, es este caso lo alberga la constante QUERYSET, para agregar este queryset, agregamos un tercer parámetro al método get, aquí le pasamos el queryset a la varaible con el nombre de _param_

## Petición vía POST
casi lo mismo pero ahora con el verbo post. Acá se necesitan los valores que van a mandar en el cuerpo de la petición. EL parámetro json convierte en un objeto json el diccionario que se le mande, esto en el método post. Para obtener algún dato de la respuesta del servidor, tenemos que volver a ejecutar el método json y acceder alguno de los atributos de este. Nos retornará los atributos solicitados que le pasamos al servidor.

## Actualizar y Eliminar
Para actualizar usamos el método put, a la url le indicamos el id de la review a modificar. Debemos envíar los nuevos datos en el cuerpo de la petición, en este caso es la review y el score. Para delete es identico, salvo el método a llamar, que sería delete.

## Cookies
Para la ruta de login también podemos tratar estas cookies. Almacenamos la ruta en una variable. Creamos un diccionario con los datos del usuario a logear y los pasamos como parámetros el método post. Si la respuesta es exitosa, damos el mensaje e imprimimos el objeto que nos retorna el servidor. Para leer de las cookies, existe el objeto cookies, lo mandamos llamar, y obtendremos un objeto del tipo RequestCookieJar, el cual lo podemos transformar en un diccionario, con el método get_dict. Para obtener la llave de la cookie, añadimos un get y especificamos la llave del diccionario.

Para obtener todas las reseñas que el cliente autenticado tiene. Mandamos la cookie al servidor por medio del parámetro cookies, al cual le pasaremos por valor un diccionario, diccionario que contendra la llave valor que acabamos de obtener.