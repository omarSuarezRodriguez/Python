num_ventas = int(input("\nIngrese el número de ventas a introducir: "))
sumaTotal = 0

for i in range(0, num_ventas):
    sumaTotal += int(input("\nIngrese el valor de la venta: "))

print("\n\nSuma total de todas las ventas: ", sumaTotal)