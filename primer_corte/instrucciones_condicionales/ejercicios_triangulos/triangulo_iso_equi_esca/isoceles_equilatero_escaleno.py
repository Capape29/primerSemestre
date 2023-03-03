# Determinar si un tríangulo es Equilátero, Isósceles, Escaleno

# Input
a = float(input("\nIngrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Processing
if a + b > c and a + c > b and b + c > a:
    if a != b and a != c and b != c:
        t = ("sí, Es posible formar un tríangulo escaleno.")
    elif a == b and a != c and b != c:
        t = ("Sí, Es posible formar un tríangulo isósceles.")
    elif a == c and a != b and c != b:
        t = ("Sí, Es posible formar un tríangulo isósceles.")
    elif b == c and b != a and c != a:
        t = ("Sí, Es posible formar un tríangulo isósceles.")
    elif a == b == c:
        t = ("Sí, Es posible formar un tríangulo Equilátero.")
else:
    t = ("No cumple con las condiciones para formar un tríangulo.")


# Output
print("\nLongitudes ingresadas")
print("Longitud a -->", a)
print("Longitud a -->", b)
print("Longitud a -->", c)
print("\n¿Se puede formar un triangulo?", t)