#
pares = 0
impares = 0

for i in range(3):
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares =impares + 1

print("Los números pares que se ingresaron fueron:", pares)
print("Los números impares que se ingresaron fueron:", impares)