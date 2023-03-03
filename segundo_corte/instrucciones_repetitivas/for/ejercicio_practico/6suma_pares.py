n = int(input("Digite el numero de terminos que quiere imprimir: "))
s = "Serie: "
#contador = 2
for i in range(1 , n + 1):
    if i < n:
        s = s + str(i * (i + 1)) + ","#contador + ","
        #contador = contador + 1
        
    else:
        s = s + str(i * i + i)#contador
        #contador = contador + 1
        i = i + i + 1
print(s)