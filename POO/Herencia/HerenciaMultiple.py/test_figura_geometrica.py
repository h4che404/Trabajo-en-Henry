from Cuadrado import Cuadrado
from Rectangulo import Figura


cuadrado1 = Cuadrado(5, "rojo")
print(cuadrado1._ancho)
print(cuadrado1._alto)
print(cuadrado1._Color)
print(cuadrado1.CalcularArea())

print(Cuadrado.mro())

print(cuadrado1)

Rectangulo1 = Figura(5, 10, "Amarillo")

print(Rectangulo1.CalcularArea())
print(Rectangulo1)