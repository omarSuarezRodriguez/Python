from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos

ventana = Tk()
ventana.title("Programa 8")
frame = ttk.Frame(ventana)

# Label 1
ttk.Label(frame, text="Números del 1 al 100 con for").pack(padx=10, pady=10)


# Evento clicked() boton
def clicked():
    for i in range(1, 101):
        textArea_1.insert(INSERT, (str(i) + "\n"))


# Boton 1
ttk.Button(frame, text="Iniciar", command=clicked).pack(padx=10, pady=10)

# TextArea 1
textArea_1 = Text(frame, width=40, height=13)
textArea_1.pack()

frame.pack(padx=10, pady=10)
guiMetodos.centrar(ventana)
ventana.mainloop()
