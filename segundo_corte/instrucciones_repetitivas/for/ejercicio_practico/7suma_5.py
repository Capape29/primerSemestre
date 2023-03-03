n = int(input("Digite el numero de terminos que quiere imprimir: "))
s = "Serie: "
for i in range(1, n + 1):
    if i < n:
        s = s + str((5 * i) - 2) + ","
    else:
        s = s + str((5 * i) - 2)
print(s)