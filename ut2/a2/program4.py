import math
import sys

radio = float(sys.argv[1])

print("(1) Calcular el diámetro de la circunferencia: d = 2*r")
print("(2) Calcular el perímetro de la circunferencia: p = 2*pi*r")
print("(3) Calcular el área del círculo: a = pi * r^2")
print("(4) Salir")


opcion = int(input("Elige una opcion:"))

if opcion >=1 and opcion <=4:
	if opcion == 1:
		d = 2 *r
		print ("Diámetro =", d)
	if opcion == 2:
		p = 2 * math.pi * radio
		print ("Perímetro =", 2 * math.pi * radio)
	if opcion == 3:
		print ("Área =", math.pi * radio^2)
	if opcion == 4:
		exit
else:
	print ("Error introduzca una opción valida")
