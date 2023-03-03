# Producto
general = "g"
afiliado = "a"
contado = "c"
plazos = "p"

# Input

cliente = str(input("ingresar 'g' si eres cliente general, sino ingresa 'a':"))
precio = int(input("Digite el precio del producto:"))
pago = str(input("ingresar 'c' si quieres pagar de contado, si quieres pagar a plazos ingresa 'p':")) 

# Prosessing
if cliente == general:
    if pago == contado:
        descuento = precio - (precio * 0.15)
    else:
        descuento = precio - (precio * 0.1)
else:
    if pago == contado:
        descuento = precio - (precio * 0.2)
    else:
        descuento = precio - (precio * 0.05)

# Output
print("El precio a cancelar es de: ", descuento, "con el descuento aplicado")
