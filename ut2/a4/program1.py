import sys

dni = int(sys.argv[1])
dni_l = "TRWAGMYFPDXBNJZSQVHLCKE"
calcular = dni % 23
calcular_letra = dni_l[calcular]

print(f"{dni}{calcular_letra}")
