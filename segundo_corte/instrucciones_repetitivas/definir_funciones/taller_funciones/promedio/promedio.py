def promediar(lista):
    contador = 0
    suma = 0
    promedio = 0
    for i in lista:
        suma = suma + i
        contador = contador + 1
    promedio = suma / contador
    return promedio

# Lista
lista = [2,3,4,5,6]
promedio = promediar(lista)
print(promedio)