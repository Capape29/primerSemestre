# Input
c = int(input("Ingrese su capital inicial: "))

# Processing
doble = 2 * c
mes = 0
while doble > c:
    c = c + 0.05 * c
    mes = mes + 1
    

# Output
print(mes)