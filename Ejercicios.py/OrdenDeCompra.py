from Producto import Producto

class Orden:
    
    id = 0

    @classmethod
    def generar_id_orden(cls):
        cls.id += 1
        return cls.id
    
    def __init__(self, productos) -> None:
        self._idOrden = Orden.generar_id_orden()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcula_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
   
    def __str__(self) -> str:
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__()
        return f"orden: {self._idOrden} \nProductos:\n {productos_str} \nEl total de los Productos es: {self.calcula_total()}"
    
if __name__ == "__main__":
    Producto1 = Producto("Harina", 25.13)
    Producto2 = Producto("Pantalon", 150.00)
    Productos1 = [Producto1, Producto2]
    Orden1 = Orden(Productos1)
    print(Orden1)