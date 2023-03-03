# Número de 4 digitos positivo

# Input 
n = int(input("Digite un numero entero: "))

# Processing
if n > 999:
    if n <= 9999:
        z = "El número ingresado, si es un número entero positivo de 4 digitos"
    else:
        z = "El número ingresado, no es un número entero positivo de 4 digitos sino de más de 4 digitos"
else:
    if n >= 0:
        z = "El número ingresado, no es un número positivo de 4 digitos sino de menos de 4 digitos"
    else:
        z = "El número ingresado, es un numero negativo"

# Output
print(z)
