# Autenticación con OAuth2
## Introducción
Es un estándar de código abierto par la autorización de aplizaciones web. Cone sto podemos asegurar los recursos de nuestra API. Existen 4 entidades presentes con OAuth2:
- Protected Resource
- Client
- Resource owner
- Authorization server

El primero es el recurso protegido, todo recurso que no queremos exponer a todos los clientes, solo a los autenticados.

El cliente, quien realiza la petición, todo tipo de dispositivo electrónico conectado a internet se considera cliente.

El propietario del recurso. En nuestro caso, son los usuarios quienes poseen reseñas y son propias de ellos, instransferibles. EXponemos los recursos del usuario autenticado.

El servidor. No hay mucho que decir, es la administración y gestión de la API.

Para que la autenticación OAuth2 se logre de manera correcta, se deben seguir los siguientes pasos:
- El usuario ingresa con sus credenciales.
- El servidore verifica que las credenciales sean correctas y retorna un __Web Token__.
- El token es guardado por el cliente.
- Las nuevas peticiones realizadas por el cleinte debe enviar el token obtenido.
- El servidor valida el token y retorna el recurso protegido.

Al hablar de OAuth2, se trabajará con __JSON Web Token (JWT)__, este objeto es una cadena alfanumérica, la cual no almacena ningun tipo de estado, es decir, stateless. Y contiene información que por sí misma valida su autenticación.

Se va a hacer este refactor de la sustitución de las cookies, porque no todos los clientes soportan el uso de cookies y claro, entre más clientes puedan usar nuestra API, mejor.

## Implementación de OAuth2
En nuestro código autual solo hay una función que usa cookies, cosa que no está bien, en vez de usar cookies con todas las rutas, usaremos OAuth2. Dentro de init del paquete app, creamos un nuevo endpoint que será para la autenticación, este se crea especificamente antes de hacer el método include_router y lo decoramos con el objeto api_v1.

Para fines práctiocos dejaremos el endpoint de login el cual retorna una cookie y el endpoint auth retornará un _JWT_.

Definimos un parámetro data que es de tipo _OAuth2PasswordRequestForm_ y su valor por defecto es una clase de nombre _Depends_, estos dos se importan de fastapi. El objeto data posee dos atributos para poder autenticar al cliente: username y password. Para ver que funciona, retornamos un diccionario con los atributos de data. En el cuerpo de la petición hay más atributos, por el momento no los vamos a definir ni usar.

## Login con OAuth
En database dentro de la clase User, crearemos un nuevo método de clase, por parámetros tiene el objeto referencia de la clase, el usuario y la contraseña. Validamos que el usuario pasado exista en la base y obtenemos el objeto user de la base, posteriormente comparamos las contraseña pasada y la que está en la base, las dos deben estar hasheadas y regresamos el usuario.

Regresamos a la función auth que estabamos trabajando e instanciamos el método de clase recién hecho con los datos que alberga el parámetro data. Y por el momento retornamos el usuario o una exepción.

## Generar access Token
Utilizaremos la librería de __PyJWT__, para instalar usamos el comando de _pip install pyjwt_. Cremos un nuevo archivo de nombre common.py, aquí importamos la librería, creamos una función para crear un token a partir de un diccionario. Por llaves tendrá el id del usuario, el nombre y la fecha de expiración del token. Fecha que es el día de la creación del token más una cantidad de días, que en este caso son 10. 

Y retornamos la llamada o respuesta del método encode de jwt, pasandole por argumentos el diccionario y un "secreto", que es una cadena alfanumérica, se debería de encriptar y con esta se podrá encriptar y desencriptar el token. Como último parámetro indicamos el algoritmo de encriptamiento a utilizar.

En init dentro de la función auth, remplazamos el retorno del usuario y su contraseña por la llamada a la función del token, dentro de un diccionario, y como segunda llave especificamos el tipo de token que le estamos mandando.

Con esto ya estaremos generando un token para los usuarios logeados, lo podremos probar en la ruta /auth. 

> Al utilizar Bearer le especificamos al cliente y a la API que estamos utilizando access token de tipo json.


## Restringir endpoints
Primero haremos un refactor a la ruta users/reviews, la cual usa cookies. En nuestra función _get reviews_ especificamos que si un cliente hace una petición a esta ruta, en el encabezado de la petición se debe mandar el access token.

En common creamos una variable que almacene un token, especificando en su primer parámetro la url de donde un usuario puede obtener su token, en nuestro proyecto es en /auth.

En get reviews pasamos como argumento el token que generamos antes, esta variable va dentro de la clase Depends.

Si todo va bien, en /docs veremos que el endpoint tiene un candado, indicando que solo los usuarios autenticados podrán acceder a esa ruta. Se debe hacer click en el candado para que se despliegue una ventana, en la cual metemos los datos de un usuario creado para que nos genere un token.

## Obtener el usuario actual
Creamos una nueva función en common.py, función que recibe el token (_get current user_). Haremos el proceso inverso a la creación de un token. A partir del token, se obtiene el diccionario con la data del usuario.

Para esto creamos otra función para decodificar el token (_decode access token_) y simplemente llamamos a decode con los mismos parámetros que el encode, NOTAR que el algoritmo a usar es una lista y ahora se llama __algorithms__ con la S.

Ahora vamos a nuestra primer función de este bloque y almacenamos el diccionario que nos regresa la funcion del token decodificado, pasandole el token que venga del usuario y regresamos el id del usuario usando una consulta con la base.

En la función get_reviews de users.py remplazamos lo que teniamos como parámetros y le pasamos un objeto del tipo User el cual va a almacenar lo que regrese nuestra funcion get_current_user. Para ver que esto funciona bien, retornamos un diccionario con el id y el username. 

Si expira nuestro token, nos dará un error en consola. Para validar la fecha de expiración, agregamos un bloque try-except en decode_access_token, y en get_current_user condicionamos si lo que alberga data es un diccionario o es un tipo None para levantar la excepción.

## Último refactor
Se obligará al cliente a tener un token para acceder a las rutas de las reviews.

Para get_reviews en users.py, retornamos el atributo reviews de los usuarios, y especificamos en el decorador que retornamos una lista de ReviewResponse.

Para create_review en reviews.py pasamos por parámetro un objeto del tipo ReviewRequest, su primer atributo es el id, pues ya no más. Ahora obtendremos el id, por medio del token. Eliminamos o comentamos ese atributo del modelo, y en la función create_review, añadimos un segundo parámetro que almacenará la respuesta de la función que nos da el diccionario con el id del usuario por medio del token. Eliminamos la primer consulta, donde verificabamos si existía el id del usuario en la base, pues esto ya lo hicimos al autenticar al usuario.

Para update_review, añadimos otro parámetro identico a lo hecho anteriormente, y dentro de la función condicionamos para ver si el id es el mismo.

Lo mismo para delete