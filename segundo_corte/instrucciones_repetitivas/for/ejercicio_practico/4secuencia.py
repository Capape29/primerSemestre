n = int(input("Digite el numero de terminos que quiere imprimir: "))
s = "Serie: "
for i in range(1 , n + 1):
    if i < n:
        s = s + str(1) + "/" + str(1 + (i - 1) * 1) + ","
    else:
        s = s + str(1) + "/" + str(1 + (i - 1) * 1)
print(s)