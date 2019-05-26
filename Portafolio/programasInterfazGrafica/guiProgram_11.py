from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos

# Estructura ventana
ventana = Tk()
ventana.title("Programa 11")
frame = ttk.Frame(ventana)

# Label 1
ttk.Label(frame, text="Generar un rango entre 0 y 10").pack(padx=10, pady=10)


# Metodo clicked() boton
def clicked():
    rango = list(range(1, 10))
    textArea_1.insert(INSERT, rango)


# Boton 1
ttk.Button(frame, text="Saber", command=clicked).pack(padx=10, pady=10)

# Text Area
textArea_1 = Text(frame, width=35, height=13)
textArea_1.pack()

# Poner frame en ventana
frame.pack(padx=10, pady=10)
guiMetodos.centrar(ventana)  # Centrar ventana
ventana.mainloop()
