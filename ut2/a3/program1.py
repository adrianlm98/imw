import sys
numero = int(sys.argv[1])
if numero >= 0:
    for primo in range(2, numero):
        resto = numero % primo
        if resto == 0:
            print("No es un numero primo")
            break
    else:
        print("Es un numero primo")
else:
    print("No puede ser un numero negativo")
