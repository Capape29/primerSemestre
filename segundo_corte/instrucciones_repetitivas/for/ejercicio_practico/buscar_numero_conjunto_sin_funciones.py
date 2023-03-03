print("--------------------------------")
print("- BUSCAR UN NÚMERO EN CONJUNTO -")
print("--------------------------------")
a = [1,2,3,4,5]
# Input
numero = int(input("Número a buscar: "))

# Processing

r = False

for i in a:
    if i == numero:
        print("Lo encontre")
        r = True
if r == False:
    print("No lo encontre")

# Output
print("\nEso era...")