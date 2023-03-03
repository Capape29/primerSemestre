# Variables
pares = 0
impares = 0

# Input
print("\nPara que el conteo de números pares e impares acabe, digite 0.")
numero = int(input("Digite un número entero: "))

# Processing 
while numero != 0:
    numero = numero % 2
    
    if numero == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    numero = int(input("Digite un número entero: "))

# Output
print("\nEl total de números pares fue de -->",pares)
print("El total de números impares fue de -->",impares)
