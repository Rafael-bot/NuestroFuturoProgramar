from tkinter import *

#Raiz
vent = Tk()
vent.title("Prueba 1")#Titulo
#vent.iconbitmap("Imagenes\Icon.ico")#Añadimos icono a la ventana
# vent.resizable(TRUE,TRUE)#Ancho y Altura. 0,0 significa que no se puede agrandar o disminui
vent.geometry("650x300")#Tamaño de la ventana
vent.config(bg="blue")

#Frame
miFrame = Frame()
miFrame.config(bg="red")#Le ponemos un color al fondo
miFrame.config(width="300", heigh="180")#Le ponemos un tamaño al frame
miFrame.config(bd="35")#Grosor del borde
miFrame.config(relief="groove")#Estilo del borde
miFrame.config(cursor="hand2")#Estio del cursor
miFrame.pack(side="left", anchor="s")
#miFrame.pack(fill="x", expand="false")#X ancho, Y altura, both y top

#Widgets


vent.mainloop()