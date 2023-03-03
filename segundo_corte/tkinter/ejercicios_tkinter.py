# Se importa la libreria tkinter con todas sus funciones

from tkinter import *

# ----------------
# Ventana pricipal
# ----------------

# Se crea una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk
ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title(" NO Estoy dentro")

# Dimensiones o tamaño de la ventana
ventana_principal.geometry("500x500")

# Desabilitar boton de maximizar
ventana_principal.resizable(0,0)

# Color de fondo de la ventana
ventana_principal.config(bg = "cyan")

# -------------------
# Frame entrada datos
# -------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "gold", width = 480, height = 240)
frame_entrada.place(x = 10, y = 10)

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "navy", width = 480, height = 120)
frame_operaciones.place(x = 10, y = 250 )

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg = "red", width = 480, height = 120)
frame_resultados.place(x = 10, y = 370)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text = "UIS Socorro")
titulo.config(bg = "black", fg = "bisque4", font = ("Arial", 80))
titulo.place(x = 240, y = 10)

# Logo de la app
logo = PhotoImage(file = "xd.png")
lb_logo = Label(frame_entrada, image = logo)
lb_logo.place(x = 61, y = 61)

# Se ejeccuta el metodo mainloop() de la clase Tk a través de la instancia ventana_principal. Esta metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (clic en un boton, escribir, etc) Cada acción del usuario se conoce como un evento. El método mainloop()es un bucle infinito.
ventana_principal.mainloop()