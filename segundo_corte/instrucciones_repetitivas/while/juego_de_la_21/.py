#input

import random
#processing
jugador=random.randint(1,10)
pc=random.randint(1,10)
dan=0
sum=0
i=1
diferencia=dan-sum
while i<= 2:
    sum=jugador
    print(sum)
    dan=dan+pc
    print(dan)
    i=i+15
print("pc",dan)
print("Jugador",sum)
print("¿Quieres seguir jugando?")
X=int(input("1. para seguir jugando o 2. para parar: "))
if X==1: 
    while sum<=21 and X!=2:
        d= random.randint(1,10)  
        sum =sum +d 
        print("jugador",sum)
        if sum>21:
            print("volaste")
            break
        print("¿Quieres seguir jugando?")
        X=int(input("1. para seguir jugando o 2. para parar: "))
        if sum>21:
            print("volaste")
            break
        elif X==2:
            while dan <=sum and dan < 21:
                p=random.randint(1,10)
                dan = dan + p
                print("pc", dan)
            if dan>sum and dan<21:
                if dan-sum==1:
                    print("El tallador gana por un punto")
                else:
                    print("gana el tallador por" , dan-sum, "Puntos")
            elif dan==sum:
                print("gana el pc por ser el tallador")
            if dan>21:
                print("El tallador ah volado")

elif X==2:
    while dan <=sum and dan < 21:
        p=random.randint(1,10)
        dan = dan + p
        print("pc", dan)
    if dan>sum and dan<21:
        if dan -sum==1:
            print("El tallador gana por un punto")
        else:
            print("gana el tallador por" , dan-sum, "Puntos")
    elif dan==sum:
        print("gana el pc por ser el tallador")
    if dan>21:
        print("El tallador ah volado")
        