import random

# Input
# Nombres de los jugadores
#jugador1 = str(input("PRIMER JUGADOR: "))
#jugador2 = str(input("SEGUNDO JUGADOR: "))

# Primera carta
carta1_jugador1 = random.randint (1, 10)
carta1_jugador2 = random.randint (1, 10)

# segunda carta
carta2_jugador1 = random.randint (1, 10)
carta2_jugador2 = random.randint (1, 10)

# Suma de las primeras dos cartas dadas
suma_jugador1 = carta1_jugador1 + carta2_jugador1
suma_jugador2 = carta1_jugador2 + carta2_jugador2

print(suma_jugador1)
print(suma_jugador2)

seguir = str(input("Quiere "))