from Empleado import *
from Gerente import *

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

Empleado1 = Gerente("Juan", 25, "San Martin")
imprimir_detalles(Empleado1)
Empleado2 = Empleado("Juan", 25.000)
imprimir_detalles(Empleado1, Empleado2)