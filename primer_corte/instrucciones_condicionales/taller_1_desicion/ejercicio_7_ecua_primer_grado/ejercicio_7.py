# Elaborar un programa para resolver una ecuación de primer grado
print("la formula de una ecuación de primer grado es --> ax + b = 0")

# Input
a = float(input("Digite el valor de la variable 'a':"))
b = float(input("Digite el valor de la variable 'b':"))

# Processing
if a != 0:
    x = -b / a
    print("La 'x' en esta ecuación tiene un valor de -->", x )
else:
    print("No se puede dividir entre cero crack")