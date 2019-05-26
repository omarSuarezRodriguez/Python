from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from programasInterfazGrafica import guiMetodos

# Variables globales
cantidad = 0
sumaTotal = 0


# Definimos clase frame1
class frame1(Frame):

    # Metodo para crear frame
    def __init__(self, miVentana):
        Frame.__init__(self, miVentana)

        # Creamos widgets
        self.label_1 = ttk.Label(miVentana, text="Sumatoria de ventas")
        self.label_2 = ttk.Label(miVentana, text="Número de ventas:")
        self.box_1 = Entry(miVentana)
        self.boton_1 = ttk.Button(miVentana, text="Iniciar", command=self.clicked_boton_1)
        self.label_3 = ttk.Label(miVentana, text="Venta #")
        self.box_2 = Entry(miVentana)
        self.boton_2 = ttk.Button(miVentana, text="Siguiente", command=self.clicked_boton_2)
        self.label_4 = ttk.Label(miVentana, text="Resultado:")

        # Ponemos widgets en frame
        self.label_1.grid(row=0, column=0, columnspan=3, padx=3, pady=3)
        self.label_2.grid(row=1, column=0, padx=3, pady=3)
        self.box_1.grid(row=1, column=1, padx=3, pady=3)
        self.boton_1.grid(row=1, column=2, padx=3, pady=3)
        self.label_3.grid(row=2, column=0, padx=3, pady=3)
        self.box_2.grid(row=2, column=1, padx=3, pady=3)
        self.boton_2.grid(row=2, column=2, padx=3, pady=3)
        self.label_4.grid(row=3, column=0, columnspan=3, padx=3, pady=3)

        # Codigo que se ejecuta la primera vez
        self.box_1.focus()
        self.box_2["state"] = "disabled"
        self.boton_2["state"] = "disabled"

    # Metodo boton 1
    def clicked_boton_1(self):

        if self.box_1.get() != "":
            global cantidad
            cantidad = int(self.box_1.get())
            print(cantidad)
            self.box_2["state"] = "normal"
            self.boton_2["state"] = "normal"
            self.box_1["state"] = "disabled"
            self.boton_1["state"] = "disabled"
            self.box_2.focus()
            self.label_3["text"] = ("Venta#" + str(cantidad))
            # self.box_1.config(state="disabled")
            self.label_4["text"] = "Resultado:"
        else:
            messagebox.showinfo("Error", "Por favor ingrese el número de ventas")
            self.box_1.focus()

    # Metodo boton 2
    def clicked_boton_2(self):

        if self.box_2.get() != "":
            global cantidad, sumaTotal

            if cantidad >= 0:
                sumaTotal += int(self.box_2.get())
                cantidad -= 1
                print(sumaTotal)
                self.label_3["text"] = ("Venta#" + str(cantidad))
                self.box_2.delete('0', END)
                self.box_2.focus()

                if cantidad == 0:
                    self.label_4["text"] = ("Resultado: " + str(sumaTotal))
                    print("Suma Total: ", sumaTotal)
                    self.box_1["state"] = "normal"
                    self.boton_1["state"] = "normal"
                    self.box_2.delete('0', END)
                    self.box_2["state"] = "disabled"
                    self.boton_2["state"] = "disabled"
                    self.box_1.delete('0', END)
                    self.box_1.focus()
                    self.label_3["text"] = "Venta #"
                    messagebox.showinfo("Resultado", ("El resultado es: " + str(sumaTotal)))
                    sumaTotal = 0

        else:
            messagebox.showinfo("Error", ("Por favor ingrese el valor de la venta #" + str(cantidad)))
            self.box_2.focus()


# Ejecutamos el codigo
ventana = Tk()
ventana.title("Programa 16")
frame_1 = frame1(ventana)
frame_1.grid(row=0, column=0)
guiMetodos.centrar(ventana)
ventana.mainloop()
