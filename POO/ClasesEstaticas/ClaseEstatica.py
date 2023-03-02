class MiClase:
    variable_clase="valor variable clase"

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
    
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


MiClase.variable_clase2 = "Valor variable clase 2"

print(MiClase.variable_clase)
miclase1 = MiClase("valor variable instancia")
print(miclase1.variable_instancia)
print(miclase1.variable_clase)
print("2do objeto".center(50, "-"))
miclase2 = MiClase("otro valor de variable instancia")
print(miclase2.variable_instancia)
print(miclase2.variable_clase)
print(miclase1.variable_clase2)

