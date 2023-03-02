class Persona:

    def __init__(self, Nombre, Apellido, Edad):
        self._Nombre = Nombre
        self._Apellido = Apellido
        self._edad = Edad
    
    #property es un decorador que permite decorar o añadir funcionalidades a la funcion.
    @property
    def nombre(self):
        return self._Nombre

    @nombre.setter
    def nombre  (self, nombre):
        self._Nombre = nombre
    
    @property
    def nombre(self):
        return self._Apellido

    @nombre.setter
    def nombre  (self, Apellido):
        self._Nombre = Apellido
    
    @property
    def nombre(self):
        return self._edad

    @nombre.setter
    def nombre  (self, edad):
        self._Nombre = edad

    def Mostrar_Dato(self):
        print(f"el nombre de la persona {self._Nombre}, el apellido de la persona {self._Apellido} y la edad {self._edad}")

    def __del__ (self):
        print(f"Se elimino el objeto con estos atributos: {self._Nombre} {self._Apellido}")
if ( __name__ == "__main__"):    
    Persona1 = Persona("juan", "martin", 25)
    Persona1.Mostrar_Dato()
    Persona1 = Persona("Pedro", "Racist", 75)
    Persona1.Mostrar_Dato()
    Persona1.nombre = "Juan Carlos"
    Persona1.Mostrar_Dato()

