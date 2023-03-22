"""Inicio"""
#todo Libreria para hacer conexiones y consultas con postgres
import psycopg2

conexion = psycopg2.connect(user="postgres",password="admin",host="127.0.0.1",port="5432",database="test_db")
try:
    #! With sirve para trabajar en algun objeto creado y 
    #! devolver un valor haciendo que la funcion termine y se cierre
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "select * from persona where id_persona in %s"
            #llaves_primarias = ((1,2,3),)
            #id_persona = input("ingrese el valor:")
            entrada = input("proporciona los id\'s a buscar (separados por comas): ")
            llaves_primarias = (tuple(entrada.split(",")),)
            cursor.execute(sentencia, (llaves_primarias,))
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f"ocurrio un error: {e}")
finally:
    conexion.close()

