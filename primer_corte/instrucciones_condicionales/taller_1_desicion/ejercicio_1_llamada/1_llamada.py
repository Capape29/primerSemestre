# Duración de una llamada

# Input
m = int(input("¿Cuantos minutos duro su llamada?: "))

# Processing
if m <= 3:
    costo = 300
else:
    costo = 300 + ( 50 * (m - 3))

# Output
print("El costo de su llamada es de: " + str(costo))
