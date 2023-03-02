class Area:
    def __init__(self, altura, base) -> None:
        self.altura = altura
        self.base = base
    def Rectangulo (self):
        return self.base * self.altura
base = int(input("ingrese el valor de la base: "))
altura = int(input("ingrese el valor de la altura: "))

objetoN1 = Area(altura, base)
print(objetoN1.Rectangulo())