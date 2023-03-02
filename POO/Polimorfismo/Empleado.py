class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self.Nombre = nombre
        self.Sueldo = sueldo

    def __str__(self) -> str:
        return f"Empleado: [Nombre: {self.Nombre} y su sueldo: {self.Sueldo}]"
    