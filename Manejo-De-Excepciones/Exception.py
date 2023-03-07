from ManejoDeExcepcionesPersonalizadas import NumerosIdenticosException
a = 0
#*las variables dinamicas se tienen que crear fuera del try-Catch

resultado = None

#*En cambio las variables si pueden usarse dentro del try-Catch

try:
    a = int(input("ingrese un numero:"))
    b = int(input("ingrese un numero distinto al primero:"))
    #*Creamos una Exception personalizada para que nos arroje un error en el caso de que sean iguales los numeros
    if a == b:
        raise NumerosIdenticosException("Numeros Identicos")
    a/b
except Exception as e:
    print(f"ocurrio un error {e}")
    print(e)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else: #*Se ejecuta en el caso de que no haya algun error.
    print("No se arrojo ningun error.")
finally: #* Se ejecuta siempre, no importa si hubo algun error o no.
    print("Se ejecuta siempre")

print(f"resultado: {resultado}")
print("continuamos...")