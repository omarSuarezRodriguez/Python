from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos

# Estructura de la ventana
ventana = Tk()
ventana.title("Programa 9")
frame = ttk.Frame(ventana)

# Label 1
ttk.Label(frame, text='Caracteres de la cadena "Hola Mundo"').pack(padx=10, pady=10)


# Evento Boton 1
def clicked():
    for i in "Hola Mundo":
        textArea_1.insert(INSERT, (i) + "\n")


# Boton 1
ttk.Button(frame, text="Saber", command=clicked).pack(padx=10, pady=10)

# Text Area
textArea_1 = Text(frame, width=35, height=13)
textArea_1.pack()


frame.pack(padx=10, pady=10)  # Ponemos frame en ventana
guiMetodos.centrar(ventana)  # Centramos ventana
ventana.mainloop()  # Loop para ventana
