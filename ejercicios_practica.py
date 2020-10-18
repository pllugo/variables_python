#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Lugo"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....
    suma = numero_1 + numero_2
    # Imprimir en pantalla el resultado de la suma
    # print(....)
    print("El valor de la suma es:", suma)

    # Repita el procedimiento para realizar la resta

    numero_1 = 5
    numero_2 = 7

    # Resta de dos numeros
    resta_num = numero_1 - numero_2

    # Imprimir por pantalla el resultado de la resta
    print("El valor de la resta es:", resta_num)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print(numero_1)
    print(numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    suma = numero_1 + numero_2
    resta_num = numero_1 - numero_2
    divide = numero_1 / numero_2
    multi = numero_1 * numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    print("El resultado de sumar", numero_1, "y", numero_2, "es", suma)
    # Resta
    print("El resultado de restar", numero_1, "y", numero_2, "es", resta_num)
    # División
    print("El resultado de dividir", numero_1, "y", numero_2, "es", divide)
    # Multiplicación
    print("El resultado de multiplicar", numero_1, "y", numero_2, "es", multi)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print("Su nombre completo es:", nombre, "", apellido)

    # Almacenar su nombre completo en una variable
    nombre_completo = nombre + " " + apellido
    print("Nombre completo en la variable:", nombre_completo)

    # Imprimir la cantidad de letras que posee su nombre completo
    print(len(nombre) + len(apellido))


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    print("El resultado del acrónimo es:", palabra_1[0] + palabra_2[0] + palabra_3[0])


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    primeras_3 = palabra_1[:3]
    print("Las tres primeras letras de la primera palabra son:", primeras_3)
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    ultimas_3 = palabra_2[-3:]
    print("Las tres últimas letras de la segunda palabra son:", ultimas_3)
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = primeras_3 + ultimas_3
    # Imprima en pantalla los resultados
    print(nueva_palabra)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
