# input
num = int(input("Digite un número: "))

# processing
if num == 0:
    num = 1
else:
    for i in range(1, num):
        num = num * i

print("Su factorial es:", num)