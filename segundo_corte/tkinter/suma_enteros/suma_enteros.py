from tkinter import *
from tkinter import messagebox

# -------------------
# Funciones de la app
# -------------------

def sumar():
    #messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar")
    z = int(x.get()) + int(y.get())
    t_resultados.insert(INSERT, "La suma de " + x.get() + "+" + y.get() + " casi simepre es " + str(z) + "\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "Hizo click en el boton salir")
    ventana_principal.destroy()


# -----------------
# Ventana principal
# -----------------

ventana_principal = Tk()
# Título de la ventana
ventana_principal.title("Sistemas UIS")

# Tamaño de la ventana
ventana_principal.geometry("500x500")
# Deshabilitar botón de maximixar
ventana_principal.resizable(0,0)

# Color de fondo de la ventana
ventana_principal.config(bg="black")

# ------------------
# Variables globales
# ------------------

x = StringVar()
y = StringVar()

# -------------------
# frame entrada datos
# -------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow", width=480, height=240)
frame_entrada.place(x=10, y=10)

# Logo de la App

logo = PhotoImage(file="xd.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=10, y=10)

# etiqueta para  el título de la app
titulo = Label(frame_entrada, text= "Suma Enteros")
titulo.config(bg="yellow", fg="blue", font=("Arial",16))
titulo.place(x=220,y=5)

# Caja de entrada de texto
tx = Label(frame_entrada, text="X = ")
tx.config(bg="yellow", fg="blue", font=("Times New Roman",16))
tx.place(x=210, y=50, width=40, height=30)

# Entrada
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="White", fg="black", font=("Times New Roman",16))
entry_x.focus_set()
entry_x.place(x=250, y=50, width=100, height=30)

# Caja de entrada de texto
ty = Label(frame_entrada, text="Y = ")
ty.config(bg="yellow", fg="blue", font=("Times New Roman",16))
ty.place(x=210, y=100, width=40, height=30)

# Entrada para y
entry_y = Entry(frame_entrada, textvariable=y)
entry_y.config(bg="White", fg="black", font=("Times New Roman",16))
entry_y.place(x=250, y=100, width=100, height=30)

# frame operaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=120)
frame_operaciones.place(x=10, y=260)

# botón para sumar
bt_sumar = Button(frame_operaciones,text="Sumar", command=sumar)
bt_sumar.place(x=45, y=45, width=100, height=30)

# botón para borrar
bt_borrar = Button(frame_operaciones,text="Borrar", command=borrar)
bt_borrar.place(x=190, y=45, width=100, height=30)

# botón para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# frame resultados
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10, y=390)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial", 20))
t_resultados.place(x=10, y=10, width=460, height=80)

# Se ejecuta el método mainloop() de la clase Tk a través de la instancia ventana principal. Este método despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escribir, etc) Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.

ventana_principal.mainloop()