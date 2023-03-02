from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento) -> None:
        super().__init__(nombre, sueldo)
        self.Departamento = departamento

    def __str__(self) -> str:
        return f"Gerente: [{self.Departamento}] {super().__str__()}"
