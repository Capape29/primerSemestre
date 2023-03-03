from tkinter import*
import random
#---------------------------
#variables globales
#---------------------------
BASE = 460
ALTURA = 460

#---------------------------
#Ventana principal
#---------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.resizable(False,False)
ventana_principal.config(bg = "green")

#-----------------------------
#frame de graficacion
#-----------------------------
frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg= "white", width=480, height=480)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creacion canva
c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)

#texto
#texto = c.create_text(BASE/2, ALTURA/2, text="Uis Socorro",font=("arial", "30","bold"), fill="blue", activefill="red" )

#lineas
#Liena1=c.create_line(0,50,BASE,ALTURA, fill = "red")
#linea2= c. create_line(0,ALTURA,BASE,0, fill= "red")

#plano
#linea3 = c.create_line(BASE/2, 0, BASE/2, ALTURA,  fill="black")
#linea4 = c.create_line(0, ALTURA/2, BASE, ALTURA/2,  fill="black")

#x = 0

#for i in range(11):
    #color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    #x = x + int(ALTURA/10)
    #linea1 = c.create_line(0,ALTURA,BASE,x,fill=color)

# Cuadrados y rectangulos
#rect1=c.create_rectangle(60,10,BASE/2-10, ALTURA,  fill="pink", outline="green")
#rect2=c.create_rectangle(10,10,110,110, fill="green")
#triangulo=c.create_polygon(10,ALTURA-10, BASE,0,BASE-10,ALTURA-10, fill="green", outline="black", width=5)
#(esquina inferior izquierda desplazamiento eje x,esquina inferior izquierda desplazamiento eje y, esquina superior desplazamiento eje x, esquina superior desplazamiento eje y, esquina inferior derecha desplazamiento eje x,esquina inferior derecha desplazamiento eje y)

#rombo
#poly2= c.create_polygon(BASE/2,0,BASE,ALTURA/2, BASE/2,ALTURA,0,ALTURA/2, fill="blue", outline="black", width=3)
#(desplazamiento esquina superior eje x, desplazamiento esquina superior eje y, desplazamiento esquina derecha eje x, deplazamiento esquiena derecha eje y, desplazamiento esquina inferior eje x, desplazamiento esquiena inferior eje y, desplazamiento esquiena izquierda eje x, desplazamiento esquina izquierda eje y)

# Elipses - Circulos
#elipse1 = c.create_oval(50 , 200,150,300, fill="pink")
#(desplazamiento lado izquierdo del circulo en eje x, desplazamiento arriba del circulo eje y, desplazamiento lado derecho eje x, deplazamiento abajo y)

# Varios circulos
for i in range(101):
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    x = random.randint(0, BASE-20)
    y = random.randint(0,ALTURA-20)
    circulo = c.create_oval(x,y,x+20,y+20,fill=color)

#arcos
#arc1 = c.create_arc(0,0, BASE,ALTURA, start= 45, extent=0, fill="red")


#for i in range(101):
    #color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    #x = random.randint(0, BASE-20)
    #y = random.randint(0,ALTURA-20)
    #arc = c.create_arc(x,y,x+20,y+20, start=45, extent= 270, fill=color)

# imagenes
#img = PhotoImage(file="balon.gif")
#balon = c.create_image(300,300, image = img, anchor = "center")
    

        #circulo_aleatorio = c.create_oval(random.randint(0,460),random.randint(0,460),BASE,ALTURA,fill=color)



ventana_principal.mainloop()