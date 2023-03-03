# Input
numero = int(input("Ingrese un número entero positivo: "))

inverso = 0
m = numero

# Processing
while numero != 0:
    digito = (numero // 10)
    r = numero - digito * 10
    inverso = inverso * 10 + r
    numero = digito

# Output
print("El número ingresado por el usuario fue:", m)
print("El inverso de ese número es:", inverso)