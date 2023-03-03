s = "Serie: "
#exponente = 0
for i in range(1, 11):
    if i < 10:
        s = s + str(i ** (i - 1)) + "/" + str(3 + (i - 1) * 2) + ","
        #exponente = exponente + 1
    else:
        s = s + str(i ** (i - 1)) + "/" + str(3 + (i - 1) * 2)
        #exponente = exponente + 1
print(s)