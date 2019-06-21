
## Dickson Omar Suarez Rodriguez

## Unipamplona

## Análisis de algoritmos



# Tuple
tuple = ('abcd', 786, 2.23, 'john', 70.2)
print(tuple[1:3])


# isupper()
c = "hola"
print(True if (c.isupper()) else False) #Operador ternario
# Resultado false


# tinyList
tinylist = [123, 'john']
print(tinylist * 2)


# Diccionario
diccionario = {'Numero': 1, 'Nombre': 'Miguel'}
print(diccionario)







################################################################




#### Punto 31


#Clase Profesor
class Profesor:
    def __init__(self, nombre, especialidad, salario):
        self.nombre = nombre
        self.especialidad = especialidad
        self.salario = salario

    #Definimos Métodos
    def obtenerNombre(self):
        print(self.nombre)

    def obtenerEspecialidad(self):
        print(self.especialidad)

    def obtenerSalario(self):
        print(self.salario)


print("\n\nPunto 31 - Profesor")

#Instanciamos el objeto
profesor1 = Profesor("Daniel", "Informatica", 3000000000)


#Imprimimos el objeto
print("Nombre: " + profesor1.nombre, " Especialidad: " + profesor1.especialidad,
      " Salario: " + str(profesor1.salario))










##############################################################


#### Punto 32


#Clase Persona
class Persona:
    def __init__(self, nombre, edad, fechaInicio):
        self.nombre = nombre
        self.edad = edad
        self.fechaInicio = fechaInicio

    # Definimos Métodos
    def obtenerNombre(self):
        print(self.nombre)

    def obtenerEdad(self):
        print(self.edad)

    def obtenerAntiguedadPersona(self):
        print(self.fechaInicio)

print("\n\nPunto 32 - Persona")

#Instanciamos Objeto
persona1 = Persona("Camilo", 30, 21032012)

#Imprimimos Objeto
persona1.obtenerNombre()
persona1.obtenerEdad()
persona1.obtenerAntiguedadPersona()









###############################################################



#### Punto 33



# Clase Triangulo
class Triangulo:

    def	__init__(self, lado1, lado2, lado3):
        self.lado1= lado1
        self.lado2= lado2
        self.lado3= lado3

    #	imprimimos
    def	imprimir(self):
        print("Los	lados	del	triángulo	tienen	el	valor	de")
        print("Lado	1:	" + str(self.lado1))
        print("Lado	2:	" + str(self.lado2))
        print("Lado	3:	" + str(self.lado3))


    #Tipo de triangulo
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triángulo equilátero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


    #Area del triangulo
    def area(self):
        print("El área del triángulo es: " + str((trianguloLado1*trianguloLado2)/2))



print("\n\nPunto 33 - Triangulos")

trianguloLado1= int(input("Ingrese el lado 1: "))
trianguloLado2= int(input("Ingrese el lado 2: "))
trianguloLado3= int(input("Ingrese el lado 3: "))

triangulo1 = Triangulo(trianguloLado1, trianguloLado2, trianguloLado3)
triangulo1.imprimir()
triangulo1.tipo()
triangulo1.area()

















































