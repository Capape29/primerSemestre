s = "Serie: " 
primos = 0 
i = 2 
 
# input 
n = int(input("Cantidad de números: ")) 
 
# processing 
while primos < n-1: 
    es_primo = True 
    for j in range(2, i): 
        if i % j == 0: 
            es_primo = False 
    if es_primo == True: 
        s = s + str(i) + "," 
        primos += 1 
    i += 1 
 
if es_primo == True: 
    s = s + str(i) 
    primos += 1 
 
# output 
print(s) 
