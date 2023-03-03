n = int(input("digite n: "))
for j in range(1,n + 1):
    sw = 0
    for i in range(2, j):
        d = n % i
        if d == 0:
            sw = 1
    if sw == 0:
        print("PRIMO")
    else:
        print("NO PRIMO")