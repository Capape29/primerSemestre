from tkinter import Tk, Canvas, Scale

ancho = 400
alto = 200
radio = 75

def modifica_arco(angulo):

    canvas.itemconfig(arco1, extent=angulo)
    #canvas.itemconfig(arco2, start=120 + int(angulo))
    #canvas.itemconfig(arco3, start=240 + int(angulo))
    

root = Tk()
root.title("Arco")
root.resizable(False, False)

canvas = Canvas(width=ancho, height=alto)
#base = canvas.create_polygon(ancho/2,alto/2,275,200,ancho/2,200,125,200, fill="black", outline="black")
arco1 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=0, fill="blue", outline="")
#arco2 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=120, extent=60, fill="red", outline="")
#arco3 = canvas.create_arc(ancho/2-radio, alto/2-radio, ancho/2+radio, alto/2+radio, start=240, extent=60, fill="yellow", outline="")


barra_deslizamiento = Scale(label='ÁNGULO', from_=0, to=360, orient="horizontal", length=ancho, command=modifica_arco, tickinterval=90)

canvas.pack()
barra_deslizamiento.pack()

root.mainloop()
