from tkinter import *
from tkinter import ttk
from programasInterfazGrafica import guiMetodos
from tkinter import messagebox

# Estructura ventana
ventana = Tk()
ventana.title("Programa 13")
frame_1 = ttk.Frame(ventana)  # Frame 1
frame_2 = ttk.Frame(ventana)  # Frame 2

# Label 1
label_1 = ttk.Label(frame_1, text="Cantidad de ventas: ")
label_1.grid(row=0, column=0)

# Box 1
box_1 = ttk.Entry(frame_1, state="enabled")
box_1.grid(row=0, column=1)
box_1.focus()

# Variables globales
cantidad = 0
sumaTotal = 0



# Metodo clicked_1() de boton_1
def clicked_1():
    global cantidad

    if box_1.get() != "":

        textArea_1.delete("1.0", END)
        box_1["state"] = "disabled"
        cantidad = int(box_1.get())
        label_2.config(text=("Venta # " + str(cantidad)))

        label_1["state"] = "disabled"
        boton_1["state"] = "disabled"
        label_2["state"] = "enabled"
        box_2["state"] = "enabled"
        boton_2["state"] = "enabled"
        box_2.focus()
        # label_1.config(text= "Hola") # Configurar Label
    else:
        messagebox.showinfo("Error", "Debe ingresar una cantidad de ventas a sumar")


# Metodo clicked_2() boton2
def clicked_2():
    global cantidad, sumaTotal
    print("Cantidad: ", cantidad)

    if box_2.get() != "":

        if cantidad >= 0:
            label_2["text"] = ("Venta # " + str(cantidad - 1))
            sumaTotal += int(box_2.get())
            # print(cantidad)
            print(sumaTotal)
            textArea_1.insert(INSERT, ("Venta #" + str(cantidad) + " =     " + box_2.get() + "\n"))
            cantidad -= 1
            box_2.delete(0, END)
            box_2.focus()

            if cantidad == 0:
                messagebox.showinfo("Fin!", ("La suma de las ventas es de: " + str(sumaTotal)))
                label_2["state"] = "disabled"
                box_2["state"] = "disabled"
                box_2.delete(0, END)
                boton_2["state"] = "disabled"
                label_1["state"] = "enabled"
                box_1["state"] = "enabled"
                boton_1["state"] = "enabled"
                box_1.focus()
                box_1.delete(0, END)
                textArea_1.insert(INSERT, ("\nLa suma de las ventas es de: " + str(sumaTotal)))
                sumaTotal = 0

    else:
        messagebox.showinfo("Error", "Debe ingresar las ventas a sumar")
        box_2.focus()


# Boton 1
boton_1 = ttk.Button(frame_1, text="Iniciar", command=clicked_1)
boton_1.grid(row=0, column=2, padx=10, pady=10)

# Label 2
label_2 = ttk.Label(frame_1, text="Venta # ")
label_2.grid(row=1, column=0)

# Box 2
box_2 = ttk.Entry(frame_1)
box_2.grid(row=1, column=1)

# Boton 2
boton_2 = ttk.Button(frame_1, text="Siguiente", command=clicked_2)
boton_2.grid(row=1, column=2)

# Scroll
scroll = ttk.Scrollbar(frame_2)
scroll.pack(side=RIGHT, fill=Y)

# Text Area
textArea_1 = Text(frame_2, width=40, height=16, yscrollcommand=scroll.set)
textArea_1.pack(side=LEFT)

# Desabilitamos widgets
label_2["state"] = "disabled"
box_2["state"] = "disabled"
boton_2["state"] = "disabled"

# Ponemos frame en ventana
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=10)
guiMetodos.centrar(ventana)  # Centramos ventana
ventana.mainloop()
