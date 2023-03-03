# Adivinar un numero
import random

numero_aleatotio = random.randint(0, 100)
intentos = 1

# Input 
numero = int(input("Trata de adivinar el numero a la primera: "))

# Processing
while numero != numero_aleatotio:
    intentos = intentos + 1

    if numero > numero_aleatotio:
        print("\nEl número que estas adivinando es menor\nVAMOS TU PUEDES")
    else:
        print("\nEl número que estas adivinando es mayor\nNOTERINDAS")
    
    numero = int(input("\nPrueba con otro número: "))


# Output
print("\nMuy bien, lo lograste.")
print("Se logro adivinar el número en", intentos, "intentos.")