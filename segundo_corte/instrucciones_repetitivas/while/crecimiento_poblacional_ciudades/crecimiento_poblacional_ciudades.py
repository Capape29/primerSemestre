# Processing
año = 1980
A = 3.5
B = 5

while A < B:
    A = A + A * 0.07
    B = B + B * 0.05
    año = año + 1

# Output
print("\nEl año en el cual la ciudad A sobrepasa en población a la ciudad B es en:", año)