print ("Mi calculadora")
# entrada

#variable a

a = float (input ("a:"))

# operaciones

print ("+. más, -. menos, *. por, /. entre")
operacion = input("signo:")

#variables b

b = float (input ("b:"))

#transformacion

if operacion == "+":
    c = a + b
    nombre = "suma"
elif operacion == "-":
    c = a - b
    nombre = "resta"
elif operacion == "*":
    c = a * b
    nombre = "multiplicacion"
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