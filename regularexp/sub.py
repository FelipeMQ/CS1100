import re

cadena_original = "CS1100-100-100-100"
cadena_nueva = re.sub("100$", "50", cadena_original, 1)
print(cadena_nueva)

patron = "Monty Python"
print(list(enumerate(patron[4::-1])))