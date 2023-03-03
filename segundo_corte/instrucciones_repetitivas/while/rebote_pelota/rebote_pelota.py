# Input
altura = float(input("Digite la altura de la pelota: "))

# Processing
ha = altura
rebotes = 0

while ha > altura / 5:
    ha -= ha * 0.1
    rebotes = rebotes + 1

# Output
print(rebotes)