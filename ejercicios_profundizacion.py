#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Lugo"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    #Se ingresa los numeros

    print('Ingrese el primer número:')
    numero_1 = float(input())

    print('Ingrese el segundo número:')
    numero_2 = float(input())

    #Se realizan las operaciones matematicas

    suma = numero_1 + numero_2 # Suma de dos números
    resta = numero_1 - numero_2 # Resta de dos números
    multiplica = numero_1 * numero_2 # Multiplicación de dos números
    divide = numero_1 / numero_2 # división de dos números
    expo = numero_1 ** numero_2 # exponente/potencia de un número

    #Aqui se realiza la impresión de las operaciones matematicas
    print("La suma entre", numero_1, "y", numero_2, "es", suma)
    print("La resta entre", numero_1, "y", numero_2, "es", resta)
    print("La multiplicación entre", numero_1, "y", numero_2, "es", multiplica)
    print("La división entre", numero_1, "y", numero_2, "es", divide)
    print("El exponente o potencia entre", numero_1, "a la", numero_2, "es",expo)


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''

    print('Ingrese su nombre/s:')
    nombre = str(input())
    print('Ingrese su apellido/s:')
    apellido = str(input())
    print('Ingrese su DNI:')
    dni = int(input()) #Este número a ingresar es un entero
    print('Ingrese su edad:')
    edad = int(input()) #Este número a ingresar es un entero
    print('Ingrese su altura (m):') #Este numero a ingresar es un decimal
    altura = float(input())
    print("Nombre Completo:", nombre + " " + apellido, ",","DNI:", dni)
    print("Nombre Completo:", nombre + " " + apellido, ",","edad:", edad, ",", "altura", altura,"m")





def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    # Como algunos nombres tienen 2 apellidos, se hace necesario preguntar si el nombre del padre y de la madre poseen 2 apellidos
    print("El nombre del padre y de la madre poseen 2 apellidos?, Responda con un Si o con No")
    # Agrego el condicional if 
    condicion = str(input())
    if condicion == "Si":
      # Aqui tanto el padre como la madre poseen 2 apellidos
      print("Ingrese el nombre completo del padre")
      nombre_padre = str(input())
      apellidos_padre = nombre_padre.split()
      print("Ingrese el nombre completo de la madre")
      nombre_madre = str(input())
      apellidos_madre = nombre_madre.split() #Almaceno en una lista con split
      print("Ingrese el nombre del hijo")
      nombre_hijo = str(input())
      nombre_completo_h = nombre_hijo + " " + apellidos_padre[2] + " " + apellidos_madre[2] #extraigo los apellidos en la posición [2] de cada lista con el split
      print("El nombre completo del hijo es:", nombre_completo_h)
    else:
      # Aqui tanto el padre como la madre poseen 1 apellido
      print("Ingrese el nombre completo del padre")
      nombre_padre = str(input())
      apellidos_padre = nombre_padre.split()
      print("Ingrese el nombre completo de la madre")
      nombre_madre = str(input())
      apellidos_madre = nombre_madre.split()
      print("Ingrese el nombre del hijo")
      nombre_hijo = str(input())
      nombre_completo_h = nombre_hijo + " " + apellidos_padre[1] + " " + apellidos_madre[1]
      print("El nombre completo del hijo es:", nombre_completo_h)

    




def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    #Se coloca end="" al final del print para que el cursor se quede en la misma linea y el usuario ingrese el nombre
    print("Ingrese el nombre de la persona 1:", end="")
    nombre_1 = str(input())
    print("Ingrese el apellido de la persona 1:", end="")
    apellido_1 = str(input())
    #Luego se suman los dos string para formar el nombre completo de la persona 1
    persona_1 = nombre_1 + " " + apellido_1
    print("El nombre completo de la persona 1 es:", persona_1)
    print("Ingrese el nombre completo (Nombre y Apellido) de la persona 2")
    persona_2 = str(input())
    #Con el uso de split() el string forma una lista o diccionario donde se le puede extraer el valor deseado, en éste caso el apellido
    apellido_2 = persona_2.split()
    #El apellido de la persona se encuentra en la posición N°=2
    apellido_persona_2 = apellido_2[1]
    condicion = apellido_persona_2 in persona_1
    # Se agrega un condicional para saber si el apellido de la persona 2 se encuentra en la variable persona_1
    if condicion == True:
      print("La persona 1 es pariente de la persona 2")
    else:
      print("La persona 1 no es pariente de la persona 2")



    
def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''
    print("Ingrese su nombre completo")
    nombre = str(input())
    print(nombre.lower()) #El nombre se imprime todo en minuscula
    print(nombre.upper()) #El nombre se imprime todo en mayuscula
    print(nombre.capitalize()) #El nombre se imprime solo mayuscula la primera letra


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
