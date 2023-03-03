numero = int(input("Ingrese un número entero: "))

# Processing
suma = 0
m = numero

while numero != 0:
    digito = (numero // 10)
    r = numero - digito * 10
    suma = suma + r
    numero = digito
    

# Output
print("El número ingresado fue -->", m)
print("La suma de los digitos del número ingresado es de:", suma)
