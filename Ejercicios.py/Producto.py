class Producto:
    
    Productoid = 0

    @classmethod
    def generarid_producto (cls):
        cls.Productoid += 1
        return cls.Productoid
    
    def __init__(self, nombre, precio) -> None:
        self._id_producto = Producto.generarid_producto()
        self._nombre = nombre
        self._precio = precio
    
    @property
    def precio (self):
        return self._precio

    def __str__(self) -> str:
        return f"\nNombre: {self._nombre} \nPrecio: ${self.precio} \nID: {self._id_producto}\n"
    

Producto1 = Producto("Harina", 25.13)
