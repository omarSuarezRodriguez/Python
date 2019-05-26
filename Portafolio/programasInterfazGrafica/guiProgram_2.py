from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana = Tk()
ventana.title("Programa 2")
# ventana.geometry("400x300+300+150")

# Label 1
ttk.Label(ventana, text="Numero 1: ", font=("Arial Bold,", 13)).grid(row=0, sticky=W)
# Label 2
ttk.Label(ventana, text="Numero 2: ", font=("Arial Bold", 13)).grid(row=1, sticky=W)
# Label 3
ttk.Label(ventana, text="Resultado: ", font=("Arial Bold", 13)).grid(row=3, sticky=W)
# Label 4
label_4 = ttk.Label(ventana, font=("Arial Bold", 13))
label_4.grid(row=3, column=1, sticky=W)

# Box 1 y 2
box_1 = ttk.Entry(ventana, width=10)
box_2 = ttk.Entry(ventana, width=10)
box_1.grid(row=0, column=1, sticky=E)
box_1.focus()
box_2.grid(row=1, column=1, sticky=E)


# sticky es para la orientacion del texto, centro izquierda o derecha
# set N, S, E, W. To align the labels to the left border, you could use W (west)

def clicked():
    resultado = int(box_1.get()) + int(box_2.get())
    label_4.config(text=resultado)  # Mostramos resultado en label
    messagebox.showinfo("Resultado: ", ("Resultado: " + str(resultado)))  # Titulo, contenido


# Boton
ttk.Button(ventana, text="Sumar", command=clicked).grid(row=2, column=1)

ventana.mainloop()
