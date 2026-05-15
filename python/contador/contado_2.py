# 1-Defino la lista

edad = [20, 23, 23, 21, 20, 21, 22, 19, 19, 20, 21, 23, 20, 21, 20, 23]

# 2-Convierto a set para eliminar repetidos y volver a lista
edad = list(set(edad)) 

# 3-Tomo el índice 0 y el índice 1 para la primera comparacion
if edad[0] >= edad[1]:
    max = edad[0]
    min = edad[1]
else:
    max = edad[1]
    min = edad[0]

# 4-Compararo el resultado con los índices restantes (del 2 en adelante)
for i in range(2, len(edad)):
    if edad[i] > max:
        max = edad[i]
    elif edad[i] < min:
        min = edad[i]

# 5-Muestro resultados
print(f"La edad MAX es {max}")
print(f"La edad MIN es {min}")
