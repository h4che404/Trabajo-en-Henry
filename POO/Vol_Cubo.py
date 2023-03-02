class VolumenDelCubo:
    def __init__(self, Largo, Alto, Ancho) -> None:
        self.Largo = Largo
        self.Alto = Alto
        self.Ancho = Ancho
    def Volumen (self):
        return self.Alto * self.Largo * self.Ancho

Largo = int(input("Ingrese el largo del cubo: "))
Alto = int(input("Ingrese el Alto del cubo: "))
Ancho = int(input("Ingrese el Ancho del cubo: "))


ObjetoN1 = VolumenDelCubo(Largo, Alto, Ancho)
print(ObjetoN1.Volumen())