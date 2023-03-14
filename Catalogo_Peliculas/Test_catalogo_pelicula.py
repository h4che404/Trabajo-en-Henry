from Dominio.Pelicula import pelicula
from Servicio.CatalogoDePeliculas import CatalagoPeliculas as cp

opcion = None


while opcion != 4:
    try:
        print("opciones:")
        print("1.Agregar Pelicula")
        print("2.Listar Pelicula")
        print("3.Eliminar Pelicula")
        print("4.Salir")
        opcion = int(input("Escribe tu opcion (1-4): "))

        
    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None
    finally:
        if opcion >= 5:
            print("Numero Equivocado de la lista de opciones")
    if opcion == 1:
        nombre_pelicula = input("ingrese el nombre de la pelicula: ")
        Pelicula = pelicula(nombre_pelicula)
        print(Pelicula)
        cp.agregar_pelicula(Pelicula)
    elif opcion == 2:
        cp.listar_peliculas()
    elif opcion == 3:
        cp.eliminar_pelicula()
    else:
        pass
else:
    print("Fin del programa")
