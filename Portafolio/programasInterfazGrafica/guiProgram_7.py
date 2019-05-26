from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos

ventana = Tk()
ventana.title("Programa 7")
frame = ttk.Frame(ventana)  # Frame


def clicked():
    c = 1
    while (c <= 100):
        textArea_1.insert(INSERT, (str(c) + "\n"))
        c += 1


# Label 1
ttk.Label(frame, text="Numeros del 1 al 100 con while").pack(padx=10, pady=10)

# Boton 1
ttk.Button(frame, text="Iniciar", command=clicked).pack(padx=10, pady=10)

# Text Area
textArea_1 = Text(frame, width=40, height=13)
textArea_1.pack()  # Ponemos text area en frame

frame.pack(padx=10, pady=10)  # Ponemos frame en ventana
guiMetodos.centrar(ventana)  # Centramos ventana

ventana.mainloop()
