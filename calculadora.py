# calculadora variable C (a+b=c)-proyecto
print ("calculadora basada en c (donde a+b=c)")
#entrados de datos(imput)
a=float (input ("valor de a:"))
b=float (input ("valor de b:"))
#definicion de variable c segun los requisitos
c=a+b
print (f"¸\nel valor de c (a+b)es:[c]")
#operaciones usando la variable c calculada
#print (/resultado de la operacion con c)
print ("suma(a+b):",a+b)
print ("resta(a-b):",a-b)
print ("multiplicacion(a*b):",a*b)
#validacion de division (por si c es 0)
if c !=0:
 print ("division (a/b):",a/b)
else:
 print ("division:no se puede dividie entre 0 (c es 0)")
print ("\n---fin de programa")

