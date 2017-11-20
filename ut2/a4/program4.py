import sys

num1 = list(sys.argv[1:])
num2 = len(num1)
sumar = 0

for i in num1:
    i = float(i)
    sumar += i
resultado = sumar / num2
print(f"La media de los valores es: {resultado}")
