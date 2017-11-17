import sys

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

if (number1 <= 0 or number2 <= 0):
    print("Los numeros no son positivos")
else:
    if (number1 < number2):
        for mcd in range(number1, 0, -1):
            if (number1 % mcd == 0 and number2 % mcd == 0):
                print("MCD de", number1, "y", number2, "=", mcd)
                break
    elif (number1 == number2):
        print("MCD de", number1, "y", number2, "=", number1)
    else:
        for mcd in range(number2, 0, -1):
            if (number2 % mcd == 0 and number1 % mcd == 0):
                print("MCD de", number1, "y", number2, "=", mcd)
                break
