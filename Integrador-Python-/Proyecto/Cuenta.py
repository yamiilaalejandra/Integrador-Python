#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
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
    
class Cuenta:

    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("Titular debe ser una instancia de la clase Persona")
        self._titular = titular
        self._cantidad = float(cantidad)
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print(f"Titular: {self._titular.nombre}")
        print(f"Cantidad: {self._cantidad:.2f}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad

titular1 = Persona(nombre="Juan Pérez", edad=30, dni="12345678A")
cuenta1 = Cuenta(titular=titular1)

cuenta1.mostrar()

cuenta1.ingresar(500.75)
cuenta1.mostrar()

cuenta1.retirar(100.25)
cuenta1.mostrar()

cuenta1.retirar(600) 
cuenta1.mostrar()