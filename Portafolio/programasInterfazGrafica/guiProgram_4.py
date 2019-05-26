from tkinter import *
from tkinter import ttk
from tkinter import messagebox


ventana = Tk()

frame = ttk.Frame(ventana)  # Creamos Frame

ventana.title("Programa 4")
# ventana.geometry("350x250")  # Tamaño ventana

### Creamos label y box y ponemos en frame

# Label 1
ttk.Label(frame, text="Número 1: ").grid(row=0, column=0, pady=5)

# Box 1
box_1 = IntVar()
ttk.Entry(frame, textvariable=box_1).grid(row=0, column=1)

# Label 2
ttk.Label(frame, text="Número 2: ").grid(row=1, column=0)

# Box 2
box_2 = IntVar()
ttk.Entry(frame, textvariable=box_2).grid(row=1, column=1)

### Mostramos frame
frame.pack(pady=5)


# Metodo Boton
def clicked():
    if box_1.get() >= box_2.get():
        messagebox.showinfo("El mayor es: ", ("Mayor: " + str(box_1.get())))  # Concatenar string con int o variable
        textArea_1.insert(INSERT, ("\nEl mayor es: " + str(box_1.get())))
    else:
        messagebox.showinfo("El mayor es: ", ("Mayor: " + str(box_2.get())))
        textArea_1.insert(INSERT, ("\nEl mayor es: " + str(box_2.get())))


### Mostramos Boton
ttk.Button(ventana, text="Saber", command=clicked).pack(pady=5)

### Mostramos Text Area
textArea_1 = Text(ventana, width=30, height=7)
textArea_1.pack(padx=10, pady=10)



ventana.mainloop()
