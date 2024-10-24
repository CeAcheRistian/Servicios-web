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