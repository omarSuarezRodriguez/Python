# Programación orientada a objetos en Python

class Pelicula:  # declarar la clase
    # Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)


# instanciar una clase
pelicula1 = Pelicula("Terminator: Destino oculto", 175, 2019)


class Catalogo:
    peliculas = []  # Declarar lista de peliculas

    # Constructor de la clase
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # Agregar objeto pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p) #Imprimir pelicula

pelicula1= Pelicula("Terminator: Destino Oculto", 175, 2019)
catalogo1 = Catalogo([pelicula1]) #Añadir la pelicula
catalogo1.mostrar()
catalogo1.agregar(Pelicula("Detective Pikachu:", 105, 2019))

