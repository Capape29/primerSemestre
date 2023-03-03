# Programa que invierte numeros de cuatro digitos

# Input
n = input("Digite un número de 4 digitos: ")
n = int(n)

# Processing
# El operador módulo no hace otra cosa que devolver el resto de la división entre los dos operandos. En el ejemplo, 7 / 2 sería 3, con 1 de resto, luego el módulo es 1.
D1 = n % 10
D2 = int((n % 100)/10)
D3 = int((n % 1000)/100)
D4 = int((n % 10000)/ 1000)

# Output 
print(D1)
print("El inverso de su numero es:" + str(D1) + str(D2) + str(D3) + str(D4))