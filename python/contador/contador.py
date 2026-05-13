# Mi contador

#1-defino mi lista

numbers = [20, 23, 23, 21, 20, 21, 22, 19, 19, 20, 21, 23, 20, 21, 22, 18]
print("contando numeros")

# uso de for para contar mi lista
for i in range (len(numbers)): 
    number_actual = numbers[i]

#conidionales para evaluar el number_actual

    if number_actual >20 :
        print (f"indice {i} :el numero {number_actual} mayor que 20")
    else :
        print (f"indice {i} :el numero {number_actual} menor que 20")


#3-logica del while

print("\n Verificando estado de conexion")

fuga = False
status = "Blue"

while fuga == False:
    if status == "Blue":
        print("Resultado: Conectado exitosamente")
        break 
    else:
        print("Resultado: Error de sistema")
         