#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre='', edad=0, dni=0):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    # Getters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def dni(self):
        return self._dni
    
    # Setters
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self._nombre = nombre
        else:
            raise ValueError("Nombre debe ser una cadena no vacía")
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("Edad debe ser un entero no negativo")
    
    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and dni:
            self._dni = dni
        else:
            raise ValueError("DNI debe ser un entero no negativo")
    
    # Métodos
    def mostrar(self):
        print(f"Nombre: {self._nombre}"+f"Edad: {self._edad}"+f"DNI: {self._dni}")
    
    def es_mayor_de_edad(self):
        return self._edad >= 18

persona1 = Persona()
persona1.nombre = "Nicolas Pérez"
persona1.edad = 30
persona1.dni = "12345678A"

persona1.mostrar()
print("Es mayor de edad:", persona1.es_mayor_de_edad())

persona2 = Persona()
persona2.nombre = "Ana García"
persona2.edad = 16
persona2.dni = "87654321B"

persona2.mostrar()
print("Es mayor de edad:", persona2.es_mayor_de_edad())
