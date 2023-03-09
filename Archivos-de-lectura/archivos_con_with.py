import os
from Manejo_archivos import ManejoArchivos
#with open("Trabajo-en-Henry/Archivos-de-lectura/prueba.txt", "r", encoding="utf8") as archivo:
#    print(archivo.read())

ruta_archivo = "Trabajo-en-Henry/Archivos-de-lectura/Prueba.txt"
if os.path.exists(ruta_archivo):
    with ManejoArchivos("Trabajo-en-Henry/Archivos-de-lectura/Prueba.txt") as archivo:
        print(archivo.read())
else:
    print("No se encontro el archivo")