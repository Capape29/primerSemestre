n = int(input("Digite el número de la secuencia: "))
s = "Serie: "
for i in range(1, n + 1):
    if i < n:
        s = s + str(1 * 2 ** (i - 1)) + ","
    else:
        s = s + str(1 * 2 ** (i - 1))
print(s)