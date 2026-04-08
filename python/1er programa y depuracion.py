def es_par(numero) : 
    if numero % 2 == 0 :
        return True
    else :
        return False
for i in range(1, 6) :
    if es_par(i) : 
        print(f"{i}es par")
else:
    print(f"{i}es impar")
        