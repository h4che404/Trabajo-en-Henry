from DispositivoEntrada import *

class ObjetoRaton (DispositivoDeEntrada):
    
    
    ID_Mouse = 0


    @classmethod
    def ContadorMouse(cls):
        cls.ID_Mouse += 1
        return cls.ID_Mouse


    def __init__ (self, tipo_entrada_Raton, MarcaRaton) -> None:
        self.IDRaton = ObjetoRaton.ContadorMouse()
        DispositivoDeEntrada.__init__(self, tipo_entrada_Raton, MarcaRaton)
        

    def __str__(self) -> str:
        return f"Se creo el mouse {self.IDRaton} {DispositivoDeEntrada.__str__(self)}"
    


