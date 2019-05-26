cadena = input("Dame una cadena: ")

cadena_al_reves = cadena[::-1]

print(cadena_al_reves)

print("Es palindromo" if cadena == cadena_al_reves else "No es palindromo")

