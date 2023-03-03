# Determinar si un tríangulo es obtuso, recto o agudo

# Input


a = float(input("\nIngrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))
print("\nIngrese los tres grados del tríangulo,'Sumados deben dar 180°'")
# Grados
d = float(input("Ingrese primer angulo del tríangulo: "))
e = float(input("Ingrese primer angulo del tríangulo: "))
f = float(input("Ingrese primer angulo del tríangulo: "))


# Processing
if a + b > c and a + c > b and b + c > a:
     
        if d + e + f == 180:
            # Triangulo recto
            if d == 90 or e == 90 or f == 90:
                if a == c and a != b and c != b or b == c and b != a and c != a or a == b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo recto e isósceles.")
                elif a != b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo recto y escaleno.")
            # Triangulo agudo
            elif d < 90 and e < 90 and f < 90:
                if a == b == c:
                    t = ("Sí, se llega a formar un tríangulo agudo y equilátero.")
                elif a == b and a != c and b != c or a == c and a != b and c != b or b == c and b != a and c != a:
                    t = ("Sí, se llega a formar un tríangulo agudo e isósceles.")
                elif a != b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo agudo y escaleno.")
            # Triangulo obtuso
            elif d > 90 and e < 90 and f < 90:
                if a == b and a != c and b != c or a == c and a != b and c != b or b == c and b != a and c != a:
                    t = ("Sí, se llega a formar un tríangulo obtuso e isósceles.")
                elif a != b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo obtuso y escaleno.")
            elif d < 90 and e > 90 and f < 90:
                if a == b and a != c and b != c or a == c and a != b and c != b or b == c and b != a and c != a:
                    t = ("Sí, se llega a formar un tríangulo obtuso e isósceles.")
                elif a != b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo obtuso y escaleno.")
            elif d < 90 and e < 90 and f > 90:
                if a == b and a != c and b != c or a == c and a != b and c != b or b == c and b != a and c != a:
                    t = ("Sí, se llega a formar un tríangulo obtuso e isósceles.")
                elif a != b and a != c and b != c:
                    t = ("Sí, se llega a formar un tríangulo obtuso y escaleno.")
        else:
            g = ("No, los angulos ingresados no suman 180 exacto.")
else:
    t = ("No, las longitudes ingresadas no llegan a formar un tríangulo.")

# Output
print("\nDatos ingresados")
print("\nLongitud a ---->", a)
print("Longitud b ---->", b)
print("Longitud c ---->", c)
print("\nPrimer grado -->", d)
print("Segundo grado ->", e)
print("Tercer grado -->", f)
print("\n¿Se logra determinar que tríangulo llega a ser?", t)
