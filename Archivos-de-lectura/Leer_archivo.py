archivo = open("Trabajo-en-Henry/Archivos-de-lectura/prueba.txt", "r", encoding="utf8")

#print(archivo.read())

#*leer algunos caracteres

#print(archivo.read(5))

#*leer lineas completas

#print(archivo.readline())

#*Iterar el archivo

#for linea in archivo:
#    print(linea)

#*leer lineas

#print(archivo.readlines())

#*acceder a alguna linea de la lista

#print(archivo.readlines()[])

#*abrimos un nuevo archivo

archivo2 = open("Trabajo-en-Henry/Archivos-de-lectura/copia.txt", "a", encoding="utf8" )
archivo2.write(archivo.read())

archivo.close()
archivo2.close()