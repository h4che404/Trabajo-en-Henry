class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad
    def __str__(self):
        return f"El nombre es: {self._nombre} y su edad es: {self._edad}"
    
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        return f"{super().__str__()} y su sueldo es: {self.sueldo}"

