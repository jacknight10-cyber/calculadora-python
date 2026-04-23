print ("Mi calculadora")
# entrada

#variable a
try:
    a = float (input ("a:")) 
except ValueError: 
    print("solo numeros")

# operaciones

print ("+. más")
print("-. menos")
print("*. por")
print("/. entre")
print("**.a la")
print("%. resto")
print("//. modulo")
operacion = input("signo:")

#variables b
try:
    b = float (input ("b:"))
except ValueError: 
    print("solo numeros")

#transformacion

if operacion == "**":
    c = a ** b
    nombre = "potencia"
elif operacion == "*":
    c = a * b
    nombre = "multiplicacion"
elif operacion == "+":
    c = a + b
    nombre = "modulo"
elif operacion == "%":
    c = a % b
    nombre = "modulo"
elif operacion == "//":
    c = a // b
    nombre = "division entera"
elif operacion == "-":
    c = a - b
    nombre = "resta"
elif operacion == "/":
    if b != 0:  
        c = a / b
        nombre = "division"
    else :
        c = "no se puede dividir por 0"
        nombre = "division"
else:
    c = "proximamente"

#salida

print("el resultado es de",c)
print ("ESO FUE TODO ESPERO QUE LES HAYA GUSTADO")