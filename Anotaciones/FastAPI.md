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
> Función que se encuentra en desuso pero para este ejemplo funciona sin problema alguno