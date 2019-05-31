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
            print(p)  # Imprimir pelicula


pelicula1 = Pelicula("Terminator: Destino Oculto", 175, 2019)
catalogo1 = Catalogo([pelicula1])  # Añadir la pelicula
catalogo1.mostrar()
catalogo1.agregar(Pelicula("Detective Pikachu:", 105, 2019))


# Herencia
class Producto:
    def __init__(self, referencia, tipo, nombre, descripcion):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion


adorno = Producto(1, 'ADORNO', 'Vaso Adornado', 'Vaso de Porcelana Rosado')

print(adorno.__dict__)  # Imprime los atributos del objeto

print(catalogo1.__dict__)

class Adorno(Producto):
    pass

adorno1 = Adorno(1, 'ADORNO', 'Vaso Adornado', 'Vaso de Porcelana Rosado')
print(adorno1.__dict__)



#Herencia multiple

class German:
    def __init_(self):
        print('OE')

    def hablarg(self):
        print('Llave')


class Paty:
    def __init__(self):
        print('Juepuerca')

    def hablarpt(self):
        print('Me encanta que grite')


class Pantera(German, Paty):
    def hablarp(self):
        print('Arrecha la joda')



pantera1 = Pantera()

pantera1.hablarg()
pantera1.hablarpt()
pantera1.hablarp()





# Trabajo Clase

# superClase Persona
class Persona:
    def __init__(self, genero, nombre):
        self.genero = genero
        self.nombre = nombre

    def obtenerNombre(self):
        print(self.nombre)

    def obtenerGenero(self):
        print(self.genero)


# clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, carnetNumero, anosDeEstudio):
        self.carnetNumero = carnetNumero
        self.anosDeEstudio = anosDeEstudio

    def obtenerCarnetNumero(self):
        print(self.carnetNumero)

    def obtenerAnosDeEstudio(self):
        print(self.anosDeEstudio)


# Clase Docente que hereda de Persona
class Docente(Persona):
    def __init__(self, especialidad):
        self.especialidad = especialidad

    def obtenerEspecialidad(self):
        print(self.especialidad)

#Creamos Objetos
persona1 = Persona("Masculino", "Daniel")
estudiante1 = Estudiante("1233234231", "3")
docente1 = Docente("Ingeniería de sistemas")

#Imprimimos Objetos
persona1.obtenerGenero()
persona1.obtenerNombre()

estudiante1.obtenerCarnetNumero()
estudiante1.obtenerAnosDeEstudio()

docente1.obtenerEspecialidad()

















