#Algoritmo para sacar los numeros pares 
#que el usuario desee usando un for
'''
n = int(input("ingrese la cantidad"))
for i in range(n):
    if (0 == i % 2):
        print(i)
'''

#Algoritmo para calcular la suma de los pares e impares que ingresemos
'''
n = int(input("ingrese la cantidad de numeros:"))
suma = 0
for i in range(n):
    num1 = int((input("ingrese un numero")))
    if (0 == num1 % 2):
        print(f"El numero {num1} es par")
    else:
        print(f"El numero {num1} es impar")
    suma += num1

print("el valor total de todos los numeros ingresados es:", suma)
'''

#Definir una lista de tipo String
'''
nombres = ['juan', 'Karla', 'Ricardo', 'Maria']
#imprimimos los nombres
print(nombres)
#imprimimos solo los nombres que seleccionamos
print(nombres[0])
print(nombres[1:3])
'''

#Crear un For que recorra del 3 a 10 incrementando de 2 en 2
'''
for i in range(3,11,2):
    print(i)

'''

