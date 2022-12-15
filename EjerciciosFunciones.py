#inicio de una funcion y de ingresar valores
'''
def mi_funcion(nombre, apellido):
    print('saludos desde mi funcion')
    print(f"nombre: {nombre} apellido: {apellido}")

mi_funcion("Juan", "Elias")
mi_funcion("Ariel", "Perez")
'''

#uso del return
'''
def sumar (a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
'''

#funcion *args que permite ingresar varios numeros y devolver valores.
'''
num = [0, 0]
for i in range(2):
    num[i] = int(input("ingrese 2 valores para ser sumados"))
    print(num[i])

def suma (*args):
    resultado = num[0] + num[1]
    return resultado



#print(suma(num[0], num[1]))
for N in range(2):
    print(suma(num[N]))

'''

#Funcion para ingresar la cantidad que quieras y multiplicar devolviendo 1 o mas valores
'''
valor = int(input("ingrese cuantos numeros quiere multiplicar"))

def multiplicar (*args):
    resultado = 1
    for i in range(valor):
        num = int(input("ingrese un numero:"))
        resultado *= num    
    return resultado, resultado

print(multiplicar())

valor = int(input("ingrese cuantos numeros quiere multiplicar"))

def multiplicar (valor):
    resultado = 1
    for i in range(valor):
        num = int(input("ingrese un numero:"))
        resultado *= num    
    return resultado, resultado
resu = {}
resu = multiplicar(valor)

print(resu)

for A in resu:
    print(A)
'''

#Funcion para ingresar 1 o mas diccionarios y devolverlos en pantalla
'''
diccionarios = {
    "JUAN" : "Nombre que sobre pasa los limites"
}

def listaDiccionario(**Terminos):
    for ID, informacion in Terminos.items():
        print(f"{ID}: {informacion }")

listaDiccionario(JUAN = "Nombre que sobre pasa los limites")
'''
#Funcion que admite mas de 1 valor y que no permite algo no iterrable
'''
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=['juan', 'karla', 'guillermo']
'''

#Factorial de 5

def factorial (numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
resultado = factorial(5)
print(f'El factorial es: {resultado}')