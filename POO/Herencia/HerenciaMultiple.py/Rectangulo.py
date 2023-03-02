from FiguraGeometrica import *
from Color import *

class Figura(FiguraGeometrica, Color):
    def __init__(self, base, altura, color) -> None:
        #super().__init__(ancho, alto)
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)
    
    def CalcularArea(self):
        return self._ancho * self._alto
    
    def __str__(self) -> str:
        return f"El Area del rectangulo es:{self.CalcularArea}, su base es: {self._ancho} y su altura es: {self._alto} y su color es: {self._Color}"