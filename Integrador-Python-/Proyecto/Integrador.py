#Escribir una función que calcule el máximo común divisor entre dos números.
num = 48
num2 = 18

def ComunDivisor(num,num2):
    while num2 != 0:
        num, num2 = num2, num % num2
    return num

#Escribir una función que calcule el mínimo común múltiplo entre dos números

def ComunMultiplo(num, num2):
    return abs(num * num2) // ComunMultiplo(num, num2)

#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    cadena = cadena.lower()
    
    import string
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    
    palabras = cadena.split()
    
    # Crear un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

cadena = input("Introduce una cadena: ")
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)


#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def contar_palabras(cadena):
    cadena = cadena.lower()
    
    import string
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    
    palabras = cadena.split()
    
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

def palabra_mas_repetida(frecuencia):
    palabra_max = max(frecuencia, key=frecuencia.get)
    return (palabra_max, frecuencia[palabra_max])

cadena = input("Introduce una cadena: ")
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)

resultado = palabra_mas_repetida(frecuencia_palabras)
print(resultado)

#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva

#implementación de la función get_int() de manera iterativa:
def get_int_iterativo():
    while True:
        try:
            valor = int(input("Introduce un número entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Por favor, introduce un número entero.")

numero = get_int_iterativo()
print(f"Has introducido el número entero: {numero}")


#Ejemplo 2 implementación de la función get_int() de manera recursiva..
def get_int_recursivo():
    try:
        valor = int(input("Introduce un número entero: "))
        return valor
    except ValueError:
        print("Valor no válido. Por favor, introduce un número entero.")
        return get_int_recursivo()

numero = get_int_recursivo()
print(f"Has introducido el número entero: {numero}")
