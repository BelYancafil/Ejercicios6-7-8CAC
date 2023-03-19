from abc import ABC, abstractmethod

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
class Persona():
   
    def __init__(self,nombre='',edad='',dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    # getters
    @property
    def nombre(self): 
        return self.__nombre 
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni
    # setters
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo
    
    @edad.setter 
    def edad(self, nuevo):
        self.__edad = nuevo
        
    @dni.setter 
    def dni(self, nuevo):
        self.__dni = nuevo

    def mostrar(self):
        return f'{self.__nombre}, {self.__edad}, {self.__dni}'
    def es_mayor_de_edad(self):
        if (self.__edad > 17 ):
            return True
        else:
            return False

print('EJERCICIO 6')        
persona_uno =Persona('bel',35,'111111')
print('PERSONA UNO')
print(f'DATOS DE LA PERSONA:{persona_uno.mostrar()}')
persona_uno.nombre='belen'
persona_uno.edad=17
persona_uno.dni='22222'
print(f'nombre:{persona_uno.nombre}')
print(f'edad:{persona_uno.edad}')
print(f'DNI:{persona_uno.dni}')
print(F'MAYOR DE EDAD:{persona_uno.es_mayor_de_edad()}')
print('PERSONA DOS')
persona_dos= Persona('','','')
persona_dos.nombre='igor'
persona_dos.edad=6
persona_dos.dni='32323'
print (f'nombre:{persona_dos.nombre}')
print(f'edad:{persona_dos.edad}')
print(f'DNI: {persona_dos.dni}')
print(f'MAYOR DE EDAD:{persona_dos.es_mayor_de_edad()}')
    
    
# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta():   
    def __init__(self,titular:Persona()='',cantidad=''):
        self.__titular = titular
        self.__cantidad = cantidad
        
    # getters
    @property
    def titular(self): 
        return self.__titular 
    @property
    def cantidad(self):
        return self.__cantidad
    
    # setters
    @titular.setter
    def titular(self, nuevo):
        self.__titular = nuevo
    
    def mostrar(self):
        return f'Titular: {self.__titular.mostrar()}, Saldo:{self.__cantidad}'

    def ingresar_dinero(self, monto):
        self.__cantidad = self.__cantidad + monto
    def retirar_dinero(self, monto):
        self.__cantidad = self.__cantidad - monto
print('--------------------------------------------------------------')
print('EJERCICIO 7')
persona_uno =Persona('bel',36,'111111')

print('PERSONA UNO')
print(F'DATOS DE LA PERSONA:{persona_uno.mostrar()}')
cuenta1 =Cuenta(persona_uno,2000)
print(F'DATOS DE LA CUENTA:{cuenta1.mostrar()}')
cuenta1.ingresar_dinero(3000)
print(F'DATOS DE LA CUENTA:{cuenta1.mostrar()}')
cuenta1.retirar_dinero(1000)
print(F'DATOS DE LA CUENTA:{cuenta1.mostrar()}')
cuenta1.retirar_dinero(5000)
print(F'DATOS DE LA CUENTA:{cuenta1.mostrar()}')
cuenta1.ingresar_dinero(3000)
print(F'DATOS DE LA CUENTA:{cuenta1.mostrar()}')

# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular: Persona() = '', cantidad='', bonificacion=''):
        super().__init__(titular, cantidad)
        self.__bonificacion= bonificacion        
    # getters
    @property
    def bonificacion(self): 
        return self.__bonificacion 
    # setters
    @bonificacion.setter
    def bonificacion(self, nuevo):
        self.__bonificacion = nuevo

    def es_titular_valido(self):
        if ((self.titular.edad >17) and (self.titular.edad < 25)):
            return True
        else:
            return False            
    
    def mostrar(self):
        return f'CUENTA JOVEN - Titular: {self.titular.mostrar()}, Saldo:{self.cantidad}, bonificacion: {self.bonificacion}%'

    
    def retirar_dinero_titular_valido(self, monto):
        if (self.es_titular_valido()):
           self.retirar_dinero(monto)
        
print('--------------------------------------------------------------')
print('EJERCICIO 8')
persona_tres =Persona('bel',23,'111111')

print('PERSONA TRES')
print(F'DATOS DE LA PERSONA: {persona_tres.mostrar()}')
cuenta1 =CuentaJoven(persona_tres,2000, 5)
print(f'ES UN TITULAR VALIDO: {cuenta1.es_titular_valido()}')
print(cuenta1.mostrar())
cuenta1.retirar_dinero_titular_valido(500)
print(cuenta1.mostrar())

persona_cuatro =Persona('PEDRITO',85,'222222')

print('PERSONA CUATRO')
print(F'DATOS DE LA PERSONA: {persona_cuatro.mostrar()}')
cuenta2 =CuentaJoven(persona_cuatro,15000, 15)
print(f'ES UN TITULAR VALIDO: {cuenta2.es_titular_valido()}')
print(cuenta2.mostrar())
cuenta2.retirar_dinero_titular_valido(500)
print(cuenta2.mostrar())
