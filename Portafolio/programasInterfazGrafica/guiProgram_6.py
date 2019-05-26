from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana = Tk()
ventana.title("Programa 6")

# Label 1
ttk.Label(ventana, text="Número: ").grid(row=0, column=0, pady=5, padx=5)

# Box 1
box_1 = ttk.Entry(ventana)
box_1.grid(row=0, column=1, padx=5)


#Evento click del boton
def clicked():
    if int(box_1.get()) >= 0 and int(box_1.get()) <= 10:
        imprimir(0, 10)
    elif int(box_1.get()) >= 11 and int(box_1.get()) <= 20:
        imprimir(11, 20)
    elif int(box_1.get()) >= 21 and int(box_1.get()) <= 30:
        imprimir(21, 30)

#Metodo para Imprimir
def imprimir(num_1, num_2):
    messagebox.showinfo("Si Está", ("El número está entre " + str(num_1) + " y " + str(num_2)))
    box_1.delete(0, END)
    box_1.focus()


# Boton
ttk.Button(ventana, text="Saber", command=clicked).grid(row=1, column=1, pady=5)

box_1.focus()
ventana.mainloop()
