class FiguraGeometrica(object):
    def __init__(self, ancho, alto) -> None:
        self._ancho = ancho
        self._alto = alto
    
    def __str__(self) -> str:
        return f"El ancho es:{self._ancho} Y el largo es:{self._alto}"

    @property
    def get_Ancho(self):
        return self._ancho
    @property
    def get_Alto(self):
        return self._alto
    @get_Ancho.setter
    def set_Ancho(self, valor):
         self._ancho = valor    
    @get_Alto.setter
    def set_Alto(self, cm):
         self._alto = cm
