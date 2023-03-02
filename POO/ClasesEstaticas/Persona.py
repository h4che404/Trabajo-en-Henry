class Persona:
    contador_personas=0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad) -> None:
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona N°{self.id_persona} Nombre:{self.nombre} edad:{self.edad} "
        
persona1 = Persona("Juan", 28)
print(persona1)
persona2 = Persona("Maria", 25)
print(persona2)