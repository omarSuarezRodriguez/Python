from tkinter import *
#from programasInterfazGrafica import guiMetodos


class frame1(Frame):

    def __init__(self, miVentana):
        Frame.__init__(self, miVentana)

        self.label_1 = Label(miVentana, text="Número 1:")
        self.box_1 = Entry(miVentana)
        self.label_2 = Label(miVentana, text="Número 2:")
        self.box_2 = Entry(miVentana)
        self.boton_1 = Button(miVentana, text="Sumar", width=20, command=self.clicked)
        self.label_3 = Label(miVentana, text="Resultado:")
        self.box_3 = Entry(miVentana)
        #Prueb

        self.label_1.grid(row=0, column=0, padx=5, pady=5)
        self.box_1.grid(row=0, column=1, padx=5, pady=5)
        self.label_2.grid(row=1, column=0, padx=5, pady=5)
        self.box_2.grid(row=1, column=1, padx=5, pady=5)
        self.boton_1.grid(row=2, column=0, padx=5, pady=5, columnspan=2)  # Se posiciona en dos columnas
        self.label_3.grid(row=3, column=0, padx=5, pady=5)
        self.box_3.grid(row=3, column=1, padx=5, pady=5)


        self.box_1.focus()
        self.box_3["state"] = "disabled"

    def clicked(self):
        resultado = int(self.box_1.get()) + int(self.box_2.get())
        self.box_3.delete(0, END)
        self.box_3["state"] = "normal"
        self.box_3.insert(INSERT, resultado)



ventana = Tk()
ventana.title("Programa 15")
frame_1 = frame1(ventana)
frame_1.grid(row=0, column=0)
#guiMetodos.centrar(ventana)
ventana.mainloop()
