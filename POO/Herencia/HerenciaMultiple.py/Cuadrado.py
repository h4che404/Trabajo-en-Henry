from FiguraGeometrica import *
from Color import *


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        #super().__init__()
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def CalcularArea(self):
        return self._alto * self._ancho

    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)} Y {Color.__str__(self)}"

