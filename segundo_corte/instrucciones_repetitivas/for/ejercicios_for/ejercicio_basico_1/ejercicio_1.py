# Ejemplos básicos instrucciones for

print("Ejercicio 1\n")
for i in (1,2,3,4,5):
    print(i)

print("Ejercicio 2\n")
for i in (1,2,3,4,5):
    print(i)

print("Ejercicio 3\n")
lista = [1,2,3,4,5]
for i in lista:
    print(i)

print("Ejercicio 4\n")
for i in range(1,6):
    print(i)

print("Ejercicio 5\n")
texto = "Uis no es uno, somos todos"
for i in texto:
    print(i)

print("Ejercicio 6: Suma 'n' primeros números")
suma = 0
for i in range(10):
    suma = suma + i
print(suma)

print("Ejercicio 7: Suma 'n' primeros números")
suma = 0
for i in range(1, 11):
    suma = suma + i
print(suma)

print("Ejercicio 8: Suma 'n' primeros números")
n = int(input("Digite el valor de 'n': "))
suma = 0
for i in range(1, n + 1):
    suma = suma + i
print(suma)

print("Ejercicio 9: Contar vocales en una frase")
frase = input("Digite una frase: ")
base = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
    if i in base:
        numero_vocales = numero_vocales + 1
print("El número de vocales es", numero_vocales)