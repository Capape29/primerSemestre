# Convertidor de segundos a horas a minutos a segundos
print("Con esta herramienta podras convertir el tiempo de segundos a horas, minutos y segundos")

# Input
S = input("Segundos a convertir: ")
S = int(S)

# Prosessing
H = S * (1 / 3600)
M = H * 60
s = M *60

# Output
print("Conversiones")
print("Segundos --> Horas:" + str(H))
print("Horas --> Minutos:" + str(M))
print("Minutos --> Segundos:" + str(s))