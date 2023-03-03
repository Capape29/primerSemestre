# Programa para calcular el área y perimetro de un circulo de x radio
import math

print("--------------------------")
print("----- Área --- Perímetro--")
print("--------------------------")

# Input del programa
r = input("Digite el valor del radio (r): ")
r = int(r)

# Processing
A = math.pi * r ** 2
P = 2 * math.pi * r

# Output
print("El área del circulo es: " + str(A))
print("El perimetro del circulo es: " + str(P))