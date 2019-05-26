def centrar(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# eliminar contenido e insertar contenido a textArea
#
# textArea_1.delete('1.0', END) # Elimina contenido
# textArea_1.insert(INSERT, (str(aleatorio) + "\n"))
