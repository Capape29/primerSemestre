# 3 números, imprimirlos en orden ascendentes

# Input
a = int(input("Digite un numero entero: "))
b = int(input("Digite un numero entero: "))
c = int(input("Digite un numero entero: "))

# Processing / Output
if a > b:
    if a > c:
        if b > c:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, b, c)
        else:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, c, b)
    else:
        print("Los tres números organizados de forma ascendente sería la siguiente:", c, a, b)
else:
    if a > c:
        print("Los tres números organizados de forma ascendente sería la siguiente:", b, a, c)
    else:
        if b > c:
            print("Los tres números organizados de forma ascendente sería la siguiente:", a, c, b)
        else:
            print("Los tres números organizados de forma ascendente sería la siguiente:", c, b, a)