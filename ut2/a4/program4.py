import sys

numbers = sys.argv[1:]
num2 = len(numbers)
sumar = 0

for i in numbers:
    i = float(i)
    sumar += i
resultado = sumar / num2
print(f"La media de los valores es: {resultado}")
