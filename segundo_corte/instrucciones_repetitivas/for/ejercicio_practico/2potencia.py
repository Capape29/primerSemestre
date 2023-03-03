n = int(input("Digite el numero de terminos que quiere imprimir: "))
s = "Serie: "
for i in range(1, n + 1):
    if i < n:
        i = i ** 2 
        s = s + str(i) + ","
    else:
        s = s + str(i**2)
print(s)