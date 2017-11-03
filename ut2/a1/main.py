import sys
money = int(sys.argv[1])

print ("El cambio de ",money, "es: ")

change_50 = money // 50
resto = money % 50

if change_50 > 0:
    print (change_50, "billetes de 50")

change_20 = resto // 20
resto = resto % 20


if change_20 > 0:
    print (change_50, "billetes de 20")

change_10 = resto // 10
resto = resto % 10


if change_10 > 0:
    print (change_10, "billetes de 10")

change_5 = resto // 5
resto = resto % 5


if change_5 > 0:
    print (change_5, "billetes de 5")

change_2 = resto // 2
resto = resto % 2


if change_2 > 0:
    print (change_2, "monedas de 2")

change_1 = resto // 1
resto = resto % 1


if change_1 > 0:
    print (change_1, "monedas de 1")

