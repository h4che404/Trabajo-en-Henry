from DispositivoEntrada import DispositivoDeEntrada

class ObjetoTeclado(DispositivoDeEntrada):
    
    ID_Teclado = 0

    @classmethod
    def ContadorTeclado (cls):
        cls.ID_Teclado += 1
        return cls.ID_Teclado
    


    def __init__(self, tipo_entrada, MarcaTeclado) -> None:
        self.IDTeclado = ObjetoTeclado.ContadorTeclado()
        DispositivoDeEntrada.__init__(self, tipo_entrada, MarcaTeclado)

    

    def __str__(self) -> str:
        return f"Se creo el Teclado {self.IDTeclado} {DispositivoDeEntrada.__str__(self)}"
    
    


