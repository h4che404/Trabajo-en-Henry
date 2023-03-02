class DispositivoDeEntrada:

    def __init__(self, tipo_entrada, Marca) -> None:
        self._tipo_entrada = tipo_entrada
        self._Marca = Marca
    


    @property
    def get_tipo_entrada (self):
        return self._tipo_entrada
    

    @get_tipo_entrada.setter
    def set_tipo_entrada (self, Nuevo_tipo_entrada):
        self._tipo_entrada = Nuevo_tipo_entrada
        return self._tipo_entrada


    @property
    def get_Marca (self):
        return self._Marca


    @get_Marca.setter
    def set_Marca (self, NuevaMarca):
        self._Marca = NuevaMarca
        return self._Marca


    
    def __str__(self) -> str:
        return f"El tipo de entrada es: {self._tipo_entrada} de la Marca: {self._Marca}"

    
if __name__ == "__main__":
    print("hello")