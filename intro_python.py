####################################################
from re import X


print("cesar compra pases")

miNumero = 5
print(miNumero)
miNumero = "cinco"
print(miNumero)

print("cesar compra pases "  + miNumero)

x = str(3)
y = int(3)
z = float(3)

print ("el tipo de dato de x es " + str(type(x)))
print ("el tipo de dato de y es "+ str(type(y))) 
print ("el tipo de dato de z es "+ str(type(z)))

edad = 30

if edad >= 18 : 
    print("mayor")
else :
    print("menor")


#listas

frutas = ["manzana", "fresa", "mango" , "guayaba"]

print (frutas[0])

print("for cycle")
indice = 0
for fruta in frutas:
    print ("indice: " + str (indice))
    print(fruta)
    indice = indice + 1

for i in range(7):
    print ("numero: " + str((i)))

for i in range(len(frutas)):
    print("fruta # " + str(i) + ": " + frutas[i]) 


#funciones

def miFuncion():
    print("hola")

miFuncion()


def myParameterFunction(palabra_uno, palabra_dos):
    print(palabra_uno + " " + palabra_dos)

myParameterFunction("aa", "si")


