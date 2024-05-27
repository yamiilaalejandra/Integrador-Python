#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

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

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            raise ValueError("Bonificación debe ser un número entre 0 y 100")
    
    def es_titular_valido(self):
        return self._titular.es_mayor_de_edad() and self._titular.edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero: el titular no es válido para esta Cuenta Joven")
    
    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven con una bonificación del {self._bonificacion}%")

# Ejemplo de uso
titular_joven = Persona(nombre="Ana García", edad=20, dni="87654321B")
cuenta_joven = CuentaJoven(titular=titular_joven, cantidad=1000.0, bonificacion=10.0)

cuenta_joven.mostrar()

print("¿Titular válido?", cuenta_joven.es_titular_valido())

cuenta_joven.ingresar(200)
cuenta_joven.mostrar()

cuenta_joven.retirar(150)
cuenta_joven.mostrar()

# Intentar retirar con un titular no válido
titular_no_valido = Persona(nombre="Pedro Martínez", edad=30, dni="12345678C")
cuenta_no_valida = CuentaJoven(titular=titular_no_valido, cantidad=500.0, bonificacion=5.0)

cuenta_no_valida.mostrar()
print("¿Titular válido?", cuenta_no_valida.es_titular_valido())

cuenta_no_valida.retirar(100)  # No se debe permitir la retirada
