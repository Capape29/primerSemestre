#
print("-------------------------------------------------------------------------------")
print("Suma de numeros enteros desde el numero 1 hasta el numero 'n' que usted desee")
print("-------------------------------------------------------------------------------")
# Input
n = int(input("ingrese 'n': "))

# Prosessing
i = 1
sum = 0 

while i <= n:
    sum = sum + i
    i = i + 1

# Output
print("La suma del número 1 hasta " + str(n), "es de:", sum)