print ("Mi calculadora")
# entrada

#variable a
a = float (input ("a:"))

# operaciones
#suma
print ("+. suma")
#resta
print ("-. resta")
#multiplicaion
print ("*.multiplicaion")
#division
print ("/. division")
operacion = input("signo de la operacion:")

#variables b
b = float (input ("\n b:"))

#transformacion
if operacion == "+":
    c = a + b
    nombre_operacion = "suma"
elif operacion == "-":
    c = a - b
    nombre_operacion = "resta"
elif operacion == "*":
    nombre_operacion = "multiplicacion"
elif operacion == "/":
    if b != 0:  
        c = a / b
        nombre_operacion = "division"
    else :
        c = "error (operacion por 0) "
        nombre_operacion = "division"

#salida
print ("\n---")
print("resultado de la", nombre_operacion)
print("es de:",c)
print ("\n---fin de programa")