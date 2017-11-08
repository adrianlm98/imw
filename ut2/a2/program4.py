import math
import sys

radio = float(sys.argv[1])

print("(1) Calcular el diámetro de la circunferencia: d = 2*r")
print("(2) Calcular el perímetro de la circunferencia: p = 2*pi*r")
print("(3) Calcular el área del círculo: a = pi * r^2")
print("(4) Salir")

opcion = int(sys.argv[2])

if opcion == 1:
	print ("Diámetro =", 2 * radio)
if opcion == 2:
	print ("Perímetro =", 2 * math.pi * radio)
if opcion == 3:
	print ("Área =", math.pi * radio^2)
if opcion == 4:
	exit
else:
	print ("Error introduzca una opción valida")