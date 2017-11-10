import sys
numero = int(sys.argv[1])

if numero >= 0:
    sumando = 0
    for suma in range(1, numero + 1):
        cuadrado = suma ** 2
        sumando += cuadrado
    else:
        print(sumando)
else:
    print("No puede ser un numero negativo")
