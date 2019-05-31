

#Programación orientada a objetos en Python

class Pelicula: #declarar la clase
    #Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)
#instanciar una clase
pelicula1 = Pelicula("Terminator: Destino oculto", 175, 2019)