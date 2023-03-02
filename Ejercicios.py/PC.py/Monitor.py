class ObjetoMonitor :

    ID_Monitor = 0

    @classmethod
    def ContadorMonitor (cls):
        cls.ID_Monitor += 1
        return cls.ID_Monitor


    def __init__(self, MarcaMonitor, TamañoMonitor) -> None:
        self.ID_Monitor = ObjetoMonitor.ContadorMonitor()
        self._Marca = MarcaMonitor
        self._Tamaño = TamañoMonitor



    @property
    def get_Marca_Monitor(self):
        return self._Marca
    
    @property
    def get_Tamaño_monitor(self):
        return self._Tamaño

    @get_Marca_Monitor.setter
    def set_Marca_Monitor (self, Marca_Monitor):
        self._Marca = Marca_Monitor
        return self._Marca
    
    @get_Tamaño_monitor.setter
    def set_Tamaño_Monitor (self, Tamaño_Monitor):
        self._Tamaño = Tamaño_Monitor
        return self._Tamaño
    

    
    def __str__(self) -> str:
        return f"Se creo el monitor Numero {self.ID_Monitor}, de marca: {self._Marca} y tamano: {self._Tamaño}'"
