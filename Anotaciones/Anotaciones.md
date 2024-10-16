# 4. Anotaciones
Para contrsuir nuestro servicio web nos apoyamos de la librería FastAPI. Está librerías e apoya de las anotaciones en Python, apra poder validar los datos de entrada y salida.

Python posee un tipado dinámico, esto quiere decir que una variable puede ser cualquier cosa y cambiar su valos n cantidad de veces. Esto no es una buena práctica, para mitigar esto, existen los Annotation types. Con esto podemos inicar de forma explicita el tipo de dato que se almacena. Se puede denotar el tipo en varaibles, funciones clases y colecciones.

> Estas anotaciones son para el lector, no para el lenguaje

- var_1: srt = 'Hola'
- var_2: int = 30
- var_3: float = 4.0
- var_4: bool = True

Para las funciones, podemos especificar el tipo de dato de los parámetros y el tipo de dato de la salida, este último se especifica con una flecha y el tipo de dato:

def suma(num1: int, num2: int) -> int:
    return num1 + num2
valor1: int = 10
valor2: int = 30
resultado: int =  suma(valo1,valor2)

Para las variables que todavía no se les asigna su valor, la sintaxis es:

variable: int

Para las clases:

-class User():  
  - def __init_(self, username:str, password:str) -> None:  
    - self.username = username  
    - self.password = password

## Colecciones
Para definir los tipos de datos para listas, tuplas, diccionarios, usamos el modulo typing de Python. Se importa y al usarse se sigue la misma sintaxis, solo que seguido de la palabra reservada se especifica el tipo de dato que contiene:

from typing import List  
calificaciones: List[int]= [10,9,7]  
def promedio(calificaciones: List[int]) -> float: