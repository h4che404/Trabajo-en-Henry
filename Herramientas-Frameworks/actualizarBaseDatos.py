import psycopg2

conexion = psycopg2.connect(user="postgres",password="admin",host="127.0.0.1",port="5432",database="test_db")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id_persona=%s"
            valores = (18,)
            cursor.execute(sentencia, valores)
            registros = cursor.rowcount
            print(f"Se actualizaron {registros} registros")
            #! El cursor es un objeto heredado de la clase psycopg2 para
            #! poder conectarse a la base de datos 
            #! y con nowcount contamos los valores que se han ingresado a la BD
except Exception as e:
    print(f"ocurrio un error: {e}")
finally:
    conexion.close()

