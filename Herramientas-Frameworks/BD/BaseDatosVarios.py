"""Inicio"""
#todo Libreria para hacer conexiones y consultas con postgres
import psycopg2

conexion = psycopg2.connect(user="postgres",password="admin",host="127.0.0.1",port="5432",database="test_db")
try:
    #! With sirve para trabajar en algun objeto creado y 
    #! devolver un valor haciendo que la funcion termine y se cierre
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre, apellido, email) values (%s, %s, %s)"
            valores = (
                ("Marcos", "Cantu", "Mcantu@gmail.com"),
                ("Angel", "quintana", "anquin@gmail.com"),
                ("Maria", "Gonzales", "mgonzales@gmail.com")
                )
            ValoresViejos = valores
            if valores != ValoresViejos:
                cursor.executemany(sentencia, valores)
                registros = cursor.rowcount
                print(f"Se agrego {registros} registros")
            else:
                print("Intento ingresar los mismos valores anteriores")
            #! El cursor es un objeto heredado de la clase psycopg2 para
            #! poder conectarse a la base de datos 
            #! y con nowcount contamos los valores que se han ingresado a la BD
except Exception as e:
    print(f"ocurrio un error: {e}")
finally:
    conexion.close()

