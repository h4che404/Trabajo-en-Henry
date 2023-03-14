class pelicula:
    
    #[]Clase especial para crear peliculas, como objeto
    
    def __init__(self, Nombre_pelicula) -> None:
        self.nombre = Nombre_pelicula
    
    def __str__(self) -> str:
        print(f"El nombre de la pelicula es: {self.nombre}")


