#
multiplos7 = 0
multiplos9 = 0

# Processing
for i in range(1000,5001):
    if i % 7 == 0:
        multiplos7 = multiplos7 + 1
    if i % 9 == 0:
        multiplos9 = multiplos9 + 1

print(multiplos7)
print(multiplos9)
