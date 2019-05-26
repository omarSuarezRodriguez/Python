from random import randint

aleatorio = randint(1, 100)
intentos = 0

while aleatorio != 0:

    numero = int(input("\n\nIngrese el número: "))

    if numero > aleatorio:
        print("\nEl numero aleatorio es menor")
        intentos += 1
    elif numero < aleatorio:
        print("\nEl numero aleatorio es mayor")
        intentos += 1
    else:
        print("\nHas ganado!")
        print("El numero aleatorio es: ", aleatorio, "\nN° Intentos: ", intentos)
        aleatorio = 0