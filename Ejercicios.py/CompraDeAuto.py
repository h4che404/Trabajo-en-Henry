class vehiculo:
    def __init__(self, Color, Ruedas) -> None:
        self.Color = Color 
        self.Ruedas = Ruedas
    def __str__(self) -> str:
        return F"su color es: {self.Color}, y sus ruedas son del tamaño: {self.Ruedas}"        

class Coche(vehiculo):
    def __init__(self, velocidad, Color, Ruedas) -> None:
        self._Velocidad = velocidad
        super().__init__(Color, Ruedas)
    def __str__(self) -> str:
        return f"La velocidad del auto es: {self._Velocidad}KM, {super().__str__()}"

class bicicleta(vehiculo):
    def __init__(self, estilo, Color, Ruedas) -> None:
        self._Estilo = estilo
        super().__init__(Color, Ruedas)
    def __str__(self) -> str:
        return f"Tiene un estilo {self._Estilo}, {super().__str__()}"


Auto1 = Coche(25, "amarrillo", 5)
print(Auto1)
bicicleta1 = bicicleta("motocross", "Rojo", 2)
print(bicicleta1)