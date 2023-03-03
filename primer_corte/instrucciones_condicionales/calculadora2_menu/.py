from tkinter import *
from tkinter import messagebox
from math import log

# --------------------------------------
# Funciones de la calculadora
# ----------------------------------------

def sumar():
    z = int(x.get()) + int(y.get())
    texto_resultados.insert(INSERT, x.get() + " + " + y.get() + " = " + str(z) + "\n")

def restar():
    z = int(x.get()) - int(y.get())
    texto_resultados.insert(INSERT, x.get() + " - " + y.get() + " = " + str(z) + "\n")

def multiplicar():
    z = int(x.get()) * int(y.get())
    texto_resultados.insert(INSERT, x.get() + " x " + y.get() + " = " + str(z) + "\n")

def dividir():
    if y.get() != 0:
        z = int(x.get()) / int(y.get())
        texto_resultados.insert(INSERT, x.get() + " - " + y.get() + " = " + str(z) + "\n")
    else:
        texto_resultados.insert(INSERT, "Math ERROR\n")
    
def potenciar():
    z = int(x.get()) ** int(y.get())
    texto_resultados.insert(INSERT, x.get() + " ^ " + y.get() + " = " + str(z) + "\n")

def logaritmo_natural():
    if int(x.get()) > 0:
        z = log(int(x.get()))
        texto_resultados.insert(INSERT, "ln" + " " + x.get() + " = " + str(z) + "\n")
    elif int(x.get()) <= 0:
        texto_resultados.insert(INSERT, "Math ERROR\n")


# Logaritmo

def AC():
    messagebox.showinfo("Calculadora 1.0", "Se borraron los datos")
    x.set("")
    y.set("")
    texto_resultados.delete("1.0", "end")

def off():
    messagebox.showinfo("Calculadora 1.0", "Esta a punto de salir")
    ventana_principal.destroy()

# -----------------
# Ventana principal
# -----------------

ventana_principal = Tk()

# Título de la ventana
ventana_principal.title("Calculadora basica")

# Tamaño de la ventana
ventana_principal.geometry("500x600")

# Deshabilitar el boton de maximizar
ventana_principal.resizable(0, 0)

# Color de fondo de la ventana
ventana_principal.config(bg = "white") # cambiar color

#
# Variables globales

x = StringVar()
y = StringVar()

#---------------------------------------------
# Frame titulo
#

frame_titulo = Frame(ventana_principal)
frame_titulo.config(bg = "black", width = 480, height = 147.5)
frame_titulo.place(x = 10, y = 10)

# Etiqueta para el titulo de la app
titulo = Label(frame_titulo, text = "Calculadora")
titulo.config(bg = "black", fg = "white" ,font = ("Calculator", 20))
titulo.place(x = 190, y = 5)

# --------------------------------------------
# Frame entrada de datos
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 460, height = 92.5)
frame_entrada.place(x = 20, y = 55)

# Caja de entrada de texto de "X"
tx = Label(frame_entrada, text = "X=")
tx.config(bg = "white", fg = "black", font = ("Calculator", 50))
tx.place(x = 20 , y = 5)

# Entrada de "X"
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg = "White", fg = "black", font = ("Calculator",20))
entry_x.focus_set()
entry_x.place(x = 70, y = 28, width = 120)

# Caja de entrada de texto de "Y"
tx = Label(frame_entrada, text = "Y=")
tx.config(bg = "white", fg = "black", font = ("Calculator", 50))
tx.place(x = 250 , y = 5)

# Entrada de "Y"
entry_x = Entry(frame_entrada, textvariable= y)
entry_x.config(bg = "White", fg = "black", font = ("Calculator",20))
entry_x.focus_set()
entry_x.place(x = 300, y = 28, width = 120)

# ------------------------------------------
# Frame operaciones
frame_botones_operaciones = Frame(ventana_principal)
frame_botones_operaciones.config(bg = "black", width = 480, height = 265)
frame_botones_operaciones.place(x = 10, y =167.5)

# Boton para sumar
boton_sumar = Button(frame_botones_operaciones, text = "+" ,font=("Calculator", 80), command=sumar)
boton_sumar.place(x = 10, y = 10, width = 75, height = 75)

# Boton para restar
boton_restar = Button(frame_botones_operaciones, text = "-", font=("Calculator", 80), command= restar)
boton_restar.place(x = 95, y = 10, width =75, height = 75)

# Boton para multiplicar
boton_multiplicar = Button(frame_botones_operaciones, text = "X", font=("Calculator", 70), command= multiplicar)
boton_multiplicar.place(x = 10, y = 95, width = 75, height = 75)

# Boton para dividir
boton_dividir = Button(frame_botones_operaciones, text = "/", font=("Calculator", 50), command= dividir)
boton_dividir.place(x = 95, y = 95, width = 75, height = 75)

# Boton para potencia
boton_potencia = Button(frame_botones_operaciones, text = "^", font=("Calculator", 60), command= potenciar)
boton_potencia.place(x = 10, y = 180, width = 75, height = 75)

# Boton para logaritmo
boton_logaritmo = Button(frame_botones_operaciones, text = "ln", font=("Calculator", 70), command= logaritmo_natural)
boton_logaritmo.place(x = 95, y = 180, width = 75, height = 75)

# Boton AC
boton_borrar = Button(frame_botones_operaciones, text = "AC", font=("Calculator", 70),command= AC)
boton_borrar.place(x = 180, y = 10, width = 290, height = 75)

# Boton off
boton_off = Button(frame_botones_operaciones, text = "off", font=("Calculator", 70), command= off)
boton_off.place(x = 180, y = 95, width = 290, height = 75)

#-------------------------------------------
# Frame resultado
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg = "black", width = 480, height = 147.5)
frame_resultado.place(x = 10, y = 442.5)

# Area de texto para resultados
texto_resultados = Text(frame_resultado)
texto_resultados.config(bg = "black", fg = "white", font = ("Calculator", 50))
texto_resultados.place(x = 10, y = 10, width = 460, height = 127.5)

#---------------------------------------------
# Ejecutar la ventana
ventana_principal.mainloop()