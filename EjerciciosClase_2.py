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