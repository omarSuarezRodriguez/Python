from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos

# Estructura ventana
ventana = Tk()
ventana.title("Programa 10")
frame = ttk.Frame(ventana)

# Label 1
ttk.Label(frame, text="Mostrar los números pares entre 1 al 100").pack(padx=10, pady=10)


# Metodo boton 1
def clicked():
    for i in range(1, 101):
        if i % 2 == 0:
            textArea_1.insert(INSERT, (str(i) + "\n"))


# Boton 1
ttk.Button(frame, text="Saber", command=clicked).pack(padx=10, pady=10)

# Scroll
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

# Text Area
textArea_1 = Text(frame, width=35, height=13, yscrollcommand=scroll.set)
textArea_1.pack(side=LEFT)

# Poner frame en ventana
frame.pack(padx=10, pady=10)
guiMetodos.centrar(ventana)
ventana.mainloop()
