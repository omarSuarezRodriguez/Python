from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Programa 3")
# ventana.geometry("400x300+300+150")

# sticky es para la orientacion del texto, centro izquierda o derecha
# set N, S, E, W. To align the labels to the left border, you could use W (west):

label_1 = ttk.Label(ventana, text="Numero 1: ")
label_1.grid(column=0, row=0)

label_2 = ttk.Label(ventana, text="Numero 2: ")
label_2.grid(column=0, row=1)

label_3 = ttk.Label(ventana, text="Resultado: ")
label_3.grid(column=0, row=4)

box_1 = ttk.Entry(ventana, width=10)
box_1.grid(column=1, row=0, sticky=W)

box_2 = ttk.Entry(ventana, width=10)
box_2.grid(column=1, row=1, sticky=W)


def clicked():
    print(int(box_1.get()) + int(box_2.get()))


boton = Button(ventana, text="Sumar", command=clicked).grid(row=3, column=0)

ventana.mainloop()
