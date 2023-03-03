def sumar_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

# Lista
lista1 = [2,3,4,5,6]
suma = sumar_datos(lista1)
print(suma) 