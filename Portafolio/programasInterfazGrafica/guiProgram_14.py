from tkinter import *


# Creamos clase con la estructura visual y metodos del frame
class frame1(Frame):
    def __init__(self, miVentana):  # Definimos el metodo del frame
        Frame.__init__(self, miVentana)

        self.label_1 = Label(miVentana, text="HelloWorld")  # Creamos label
        self.label_1.pack()  # Lo mostramos en el frame

    def hola(self):  # Definimos un  metodo
        print("Hola")


ventana = Tk()
frame_1 = frame1(ventana)
frame_1.pack()
frame_1.label_1.config(text="Madre")
frame_1.hola()
frame_1.label_1["text"] = "Madrazo"
ventana.mainloop()
