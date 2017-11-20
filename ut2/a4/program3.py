import sys

k = int(sys.argv[1])
texto = str(sys.argv[2])

if k < 0:
    sys.exit("Tiene que ser positivo")
else:
    texto_a = texto.split(" ")
    sumar = 0
for i in texto_a:
    if len(i) == k:
        sumar += 1
print(f"Hay {sumar} palabras de tamaño {k}")
