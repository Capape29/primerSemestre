# Dados tres (3) números a, b, c. Verificar si pueden formar los lados de un tríangulo

# Input
a = int(input("Ingrese el primer lado del triángulo: "))
b = int(input("Ingrese el segundo lado del triángulo: "))
c = int(input("Ingrese el tercer lado del triángulo: "))

# Processing
if a + b > c and a + c > b and b + c > a:
    print("Sí se puede llegar a formar un triángulo")
elif a == b == c:
    print("Sí se puede llegar a formar un triángulo")
else:
    print("No se puede llegar a formar un triángulo con esos valores")