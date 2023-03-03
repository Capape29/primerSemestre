# Input
cheque = int(input("Ingrese el valor de su cheque: "))
ch = cheque
# Valor de los billetes / monedas
# billetes1 = 10000
# billetes2 = 2000
# monedas = 100

# Contador de billetes
total_billetes1 = 0
total_billetes2 = 0
total_monedas = 0

# Processing
while cheque != 0:
    billetes1 = cheque // 10000
    restante = cheque - billetes1 * 10000
    billetes2 = restante // 2000
    restante = restante - billetes2 * 2000
    monedas = restante // 100
    total_billetes1 = total_billetes1 + billetes1
    total_billetes2 = total_billetes2 + billetes2
    total_monedas = total_monedas + monedas

    print("El valor del cheque es de:", ch)
    print("Billetes de $10.000 a entregar:", billetes1)
    print("Billetes de $2.000 a entregar:", billetes2)
    print("Monedas de 100 a entregar:", monedas)
    print("\nGRACIAS POR SU VISITA\nVUELVA PRONTO\n")

    cheque = int(input("Ingrese el valor de su cheque: "))

# Output
print("Billetes de $10.000 que se entregaron en el día fueron de:", total_billetes1)
print("Billetes de $2.000 que se entregaron en el día fueron de:", total_billetes2)
print("Monedas de $100 que se entregaron en el día fueron de:", total_monedas)