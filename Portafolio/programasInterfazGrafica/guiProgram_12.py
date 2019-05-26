from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos
from random import randint

# Estructura ventana
ventana = Tk()
ventana.title("Programa 12")
frame = ttk.Frame(ventana)

# Label 1
ttk.Label(frame, text="Generar un número entre 5 y 10").pack(padx=10, pady=10)


# Metodo clicked() boton 1
def clicked():
    aleatorio = randint(5, 10)
    textArea_1.delete('1.0', END)  # Elimina contenido
    textArea_1.insert(INSERT, (str(aleatorio) + "\n"))  # Inserta contenido


# Boton 1
ttk.Button(frame, text="Saber", command=clicked).pack(padx=10, pady=10)

# Text Area
textArea_1 = Text(frame, width=33, height=13)
textArea_1.pack()

# Poner frame en ventana
frame.pack(padx=10, pady=10)
guiMetodos.centrar(ventana)  # Centrar ventana
ventana.mainloop()
