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

Ingresos = [2500, 4000, 1000]
total = 0
for i in range(2):
    total += Ingresos[i]
print("Estos son mis ingresos del mes:", total)
print("Mis gastos fueron en: Navidad Green, Salir a comer y tomar helado, pagar world.")
print("Cuanta plata me queda?")
print("-1000")