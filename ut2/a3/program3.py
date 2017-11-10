import sys
numero = int(sys.argv[1])
if numero >= 0:
    valor = 1
    for i in range(1, numero + 1):
        valor = i * valor
        print(i, "! =", valor)
else:
    print("No puede ser un numero negativo")
