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