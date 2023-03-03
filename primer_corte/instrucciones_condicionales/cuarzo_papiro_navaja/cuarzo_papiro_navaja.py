# Cuarzo Papiro Navaja (Maquina vs. Humano)

import random

# Maquina
maquina = random.randint(1,3)
bot = input("Ingresa el nombre de tu contrincante: ")
#bot = str("Bot")
usuario = input("Cuál es tu nombre guerrero?: ")

# Input 
print("\nArmas a utilizar en combate\n")
# Se despliega el arsenal de armas
print("1. Cuarzo (Piedra)")
print("2. Papiro (Papel)")
print("3. Navaja (Tijera)")

opcion = int(input("\nEscoge tu arma para el combate: "))

# Processing
if (opcion == 1 and maquina == 1):
    print(bot, "--> Cuarzo (Piedra)")
    print(usuario, "--> Cuarzo (Piedra)")
    r = print("¡QUE GRAN EMPATE!")
elif (opcion == 1 and maquina == 2):
    print(bot, "--> Papiro (Papel)")
    print(usuario, "--> Cuarzo (Piedra)")
    r = print("YOU LOSEEEEEE")
elif (opcion == 1 and maquina == 3):
    print(bot, "--> Navaja (Tijeras)")
    print(usuario, "--> Cuarzo (Piedra)")
    r = print("VICTORIA ROYAL")
elif (opcion == 2 and maquina == 1):
    print(bot, "--> Cuarzo (Piedra)")
    print(usuario, "--> Papiro (Papel)")
    r = print("VICTORIA ROYAL")
elif (opcion == 2 and maquina == 2):
    print(bot, "--> Papiro (Papel)")
    print(usuario, "--> Papiro (Papel)")
    r = print("¡QUE GRAN EMPATE!")
elif (opcion == 2 and maquina == 3):
    print(bot, "--> Navaja (Tijeras)")
    print(usuario, "--> Papiro (Papel)")
    r = print("YOU LOSEEEEEE")
elif ( opcion == 3 and maquina == 1):
    print(bot, "--> Cuarzo (Piedra)")
    print(usuario, "--> Navajas (Tijeras)")
    r = print("YOU LOSEEEEEE")
elif (opcion == 3 and maquina == 2):
    print(bot, "--> Papiro (Papel)")
    print(usuario, "--> Navajas (Tijeras)")
    r = print("VICTORIA ROYAL")
elif (opcion == 3 and maquina == 3):
    print(bot, "--> Navaja (Tijeras)")
    print(usuario, "--> Navajas (Tijeras)")
    r = print("¡QUE GRAN EMPATE!")
else:
    print("No escogiste tu arma guerrero")