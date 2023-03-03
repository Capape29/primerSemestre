def mostrar_cadena(cadena, repeat):
    for i in range(repeat):
        print(cadena)

# Input
cadena = input("digite cadena de texto: ")
repeat = int(input("Número de veces que desea repetir la cadena"))
mostrar_cadena(cadena, repeat)