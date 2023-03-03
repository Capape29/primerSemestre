def promediar_pares(lista):
    contador = 0
    suma = 0
    promedio = 0
    for i in lista:
        if i % 2 == 0:
            suma = suma + i
            contador = contador + 1
    promedio = suma / contador
    return promedio

# Lista
lista = [2,3,4,5,6]
promedio = promediar_pares(lista)
print(promedio)