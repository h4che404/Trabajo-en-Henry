'''
#1
var = 1
print(var)
#2
print("--------------------------------")
var1 = 8.5
print(type(var1))
#3
print("--------------------------------")
print(var)
#4
print("--------------------------------")
nombre = "juan"
#5
print("--------------------------------")
num = 9123.123423
#6
print("--------------------------------")
print(type(num))
#7
print("--------------------------------")
palabra = "juan"
mensaje = palabra.find("a")
print (mensaje)
#8
print("--------------------------------")
x = 0
while x < 3:
    x += 1
    print(x)
print("fin")
#9
print("--------------------------------")
for i  in range(2):
    nombre1 = input("ingrese un nombre")
    edad= input ("ingrese su edad")
    print("Hola {}, usted tiene {}?".format(nombre1, edad))
print("fin")
#10
print("--------------------------------")
print("listas y vectores")

nombres = ['juan', 'karla', 'ricardo']

for i in range(11):
    if i % 3 == 0 :
        print(i)

print("--------------------------------")
print("Listas y tuplas ()")

frutas = ("Naranja", "Pera", "Manzana")

for fruta in frutas:
    print(fruta)

frutaLista = list(frutas)
frutaLista[0] = "Mandarina"
frutas = tuple(frutaLista) 

for fruta in frutas:
    print(fruta)

print("--------------------------------")
print("EjercicioTupla")

tupla = (13, 1, 8, 3, 2, 5, 8)

for elemento in tupla:
    if (elemento < 5):
        print(elemento)
'''
#Definir una lista de tipo String
'''
nombres = ['juan', 'Karla', 'Ricardo', 'Maria']
#imprimimos los nombres
print(nombres)
#imprimimos solo los nombres que seleccionamos
print(nombres[0])
print(nombres[1:3])
nombres[3] = 'Marcos'
print(nombres[3]) 

for i in nombres:
    print(i)

'''

#Diccionario
Diccionario = {
    'IDE':"intregrated Development Environment",
    'OOP':"Object Oriented Programming"
}

print(Diccionario)

#Largo

print(len(Diccionario))

for ID, Informacion in Diccionario.items():
    print(ID, Informacion)

for ID in Diccionario.keys():
    print(ID)

for Informacion in Diccionario.values():
    print(Informacion)

print("IDE" in Diccionario)

Diccionario["PK"] = "Prymary key"

