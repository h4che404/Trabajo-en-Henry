from Raton import *
from Teclado import *
from Monitor import *

class Computadora (ObjetoRaton, ObjetoTeclado, ObjetoMonitor):

    ID_Computadora = 0

    @classmethod
    def ContadorDeComputadoras (cls):
        cls.ID_Computadora += 1
        return cls.ID_Computadora
    


    def __init__(self, Nombre, MarcaMonitor, TamañoMonitor, MarcaTeclado, tipo_entrada_Teclado, tipo_entrada_Raton, MarcaRaton) -> None:
        self._ID_Computadora = Computadora.ContadorDeComputadoras()
        self._nombre = Nombre
        ObjetoMonitor.__init__(self, MarcaMonitor, TamañoMonitor)
        ObjetoTeclado.__init__(self, tipo_entrada_Teclado, MarcaTeclado)
        ObjetoRaton.__init__(self, tipo_entrada_Raton, MarcaRaton)


    def __str__(self) -> str:
        return f'''
        Nombre: {self._nombre}
        Numero de Identificacion: {self._ID_Computadora}
        Monitor: {ObjetoMonitor.__str__(self)} 
        Teclado: {ObjetoTeclado.__str__(self)}
        Raton: {ObjetoRaton.__str__(self)}
        
        '''
    
computadora1 = Computadora("PC1", "ACER", 25, "Redragon", "USB", "USB", "NOGA")
print(computadora1)