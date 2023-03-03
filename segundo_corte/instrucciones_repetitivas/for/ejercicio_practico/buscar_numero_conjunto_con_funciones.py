# Definición de la función
def buscarDatosEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

# Entrada
dato = int(input("Número a buscar: ")) # Se recibe el dato del usuario

# Processing
lista = [1,2,3,4,5] # Se almacena una lista de datos
if buscarDatosEnLista(dato, lista):
    print("Lo encontre")
else:
    print("no lo encontre")

# Output
print("\nEso era...")
