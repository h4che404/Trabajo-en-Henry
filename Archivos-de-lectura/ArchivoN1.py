#Aprendemos a crear y leer archivos desde python
try:
    archivo = open("Trabajo-en-Henry/Archivos-de-lectura/Prueba.txt", "w", encoding="utf8")
    archivo.write("Agregamos información al archivo \n")
    archivo.write("Adios")
    
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("Se cerro el archivo")
    #*No se puede agregar informacion 
    #*despues de cerrar el archivo
    archivo.write("Nueva info")

