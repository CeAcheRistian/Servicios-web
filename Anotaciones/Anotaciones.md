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

- class User():  
  - def __init_(self, username:str, password:str) -> None:  
    - self.username = username  
    - self.password = password

## Colecciones
Para definir los tipos de datos para listas, tuplas, diccionarios, usamos el modulo typing de Python. Se importa y al usarse se sigue la misma sintaxis, solo que seguido de la palabra reservada se especifica el tipo de dato que contiene entre corchetes. Si se quiere denotar explicitamente cada uno de los elementos de la coleccion, usamos Union:

from typing import List, Tuple, Dict, Union  
calificaciones: List[int]= [10,9,7]  
def promedio(calificaciones: List[int]) -> float:  
config: Tuple[str] = ('localhost', '8000')  
usuarios: Dict[str, int] = { 'Chris': 10, 'Kari': 10 }  
mi_tupla: Tuple[Union[str, bool, int]] = ('hola', True, 67)  

> Proseguimos a tipear todo el codigo que tenemnos hasta el momento.

## Pydantic
Librería usada por FastAPI, esta librería permite validar datos de entrada como los de salida. Las validaciones se implementan usando anotaciones o typing.  
Veremos una introducción para implementar nuestras validaciones utilizando modelos.  
Se requiere instalar, así pues: _pip install pydantic_

Para validar los datos, heredamos de la clase BaseModel. En los atributos de la clase especificamos el tipo de dato. Al instanciar la clase **Debemos** pasar los tipos de dato correctos o se quejará, en algunos casos transformara los tipos de datos que le pasemos al correcto. Si le pasamos un entero y lo que recibe son cadenas de texto, entonces transforma el entero a cadena de texto. Si le pasamos un booleano y recibe un entero, entonces regresará un 0 o 1.

Con BaseModel si o si se cumplen las anotaciones, además que todos los atributos de la clase son obligatorios, si no le damos un valor al momento de instanciarlo habrá error. Si necesitamos que alguno de los valores sea opcional, entonces importamos _Optional_ de typing, y especificamos el tipo de valor que puede recivir, por default es None.

from pydantic import BaseModel  
from typing import Optional  
- class User(BaseModel):  
  - name: str  
  - pass:str  
  - age: Optional[int] = None  
user1 = User(name=10, pass="pass123", age=27)

## Validaciones propias