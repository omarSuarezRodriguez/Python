from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana = Tk()
ventana.title("Programa 5")

# Label 1
ttk.Label(ventana, text="Número: ").grid(row=0, column=0, pady=5, padx=5)

# Box 1
box_1 = ttk.Entry(ventana)
box_1.grid(row=0, column=1, padx=5)


def clicked():
    if int(box_1.get()) >= 0 and int(box_1.get()) <= 10:
        messagebox.showinfo("Si Está", "El número si está entre 0 y 10")
        box_1.delete(0, END)
        box_1.focus()


# Boton
ttk.Button(ventana, text="Saber", command=clicked).grid(row=1, column=1, pady=5)

box_1.focus()
ventana.mainloop()
