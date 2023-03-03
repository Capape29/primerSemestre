# Convertidor de °C --> K y °C --> °F

# Input
C = input("Digite los grados centigrados a convertir (°C): ")
C = int(C)

# Prosessing
K = 273.15 + C
F = 9 / 5 * C + 32

# Output
print("celcius a Kelvin --> " + str(K))
print("Celcius a Farenheit --> " + str(F))
