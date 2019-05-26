from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Programa 1")
ventana.geometry("300x200+300+150")

label_1= ttk.Label(ventana, text="Hola mundo").pack()



ventana.mainloop()
