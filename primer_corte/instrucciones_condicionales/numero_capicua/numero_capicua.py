# Leer un número entero de 5 digitos y determinar si es capiúa
print("---------------------------------")
print("Un número capiúa se refiere a cualquier número que se lee igual de izquierda a derecha que de derecha a izquierda. Ejemplos: 161, 2992, etc.")
print("---------------------------------")

# Input
n = int(input("Digite un numero entero:"))

# Processing / Output
if n >= 10000:
    if n < 100000:
        e = n % 10
        d = (n % 100)//10
        b = (n % 10000) // 1000
        a = (n % 100000) // 10000
        if a == e:
            if b == d:
                print("El número ingresado es de 5 digitos y tambien es capicúa -->", n)
            else:
                print("El número ingresado es de 5 digitos pero no es capicúa -->", n)
        else:
            print("El número ingresado es de 5 digitos pero no es capicúa -->", n)
    else:
        print("El número es mayor de 5 digitos -->", n)
else:
    print("El número ingresado no es de 5 digitos -->", n)