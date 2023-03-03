import random

# contadores de números del dado
d1 = " "
d2 = " "
d3 = " "
d4 = " "
d5 = " "
d6 = " "

# Input

numero_l = int(input("Cuantas veces quiere lanzar el dado? "))

for i in range (numero_l):
    lanzamientos = random.randint(1,6)
    if lanzamientos == 1:
        d1 = d1 + "*"
    elif lanzamientos == 2:
        d2 = d2 + "*"
    elif lanzamientos == 3:
        d3 = d3 + "*"
    elif lanzamientos == 4:
        d4 = d4 + "*"
    elif lanzamientos == 5:
        d5 = d5 + "*"
    elif lanzamientos == 6:
        d6 = d6 + "*"
    
print("El número de veces que salio 1 fue:", d1)
print("El número de veces que salio 2 fue:", d2)
print("El número de veces que salio 3 fue:", d3)
print("El número de veces que salio 4 fue:", d4)
print("El número de veces que salio 5 fue:", d5)
print("El número de veces que salio 6 fue:", d6)
