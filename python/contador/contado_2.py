# la lista

edad = [20, 23, 23, 21, 20, 21, 22, 19, 19, 20, 21, 23, 20, 21, 20, 23]

edad = list(set(edad)) 

if edad[0] >= edad[1]:
    max = edad[0]
    min = edad[1]
else:
    max = edad[1]
    min = edad[0]


for i in range(2, len(edad)):
    if edad[i] > max:
        max = edad[i]
    elif edad[i] < min:
        min = edad[i]

# resultados
print(f"La edad MAX es {max}")
print(f"La edad MIN es {min}")
