
import sys
money = sys.argv[1]

print (money)

money_50 = money % 50
money_50x = money // 50

if money_50x > 0:
    print (money_50x, "billete/s de 50")
else:
    print ("Ninguno de 50")

money_20 = money_50 % 20
money_20x = money_50 // 20

if money_20x > 0:
    print (money_20x, "billete/s de 20")
else:
    print ("Ninguno de 20")

money_10 = money_20 % 10
money_10x = money_20 // 10

if money_10x > 0:
    print (money_10x, "billete/s de 10")
else:
    print ("Ninguno de 10")

money_5 = money_10 % 5
money_5x = money_10 // 5

if money_5x > 0:
    print (money_5x, "billete/s de 5")
else:
    print ("Ninguno de 5")

money_2 = money_5 % 2
money_2x = money_5 // 2

if money_2x > 0:
    print (money_2x, "moneda/s de 2")
else:
    print ("Ninguno de 2")

money_1 = money_2 % 1
money_1x = money_2 // 1

if money_1x > 0:
    print (money_1x, "moneda/s de 1")
else:
    print ("Ninguno de 1")


money_50 = money % 50
money_50x = money // 50

if money_50x > 0:
    print (money_50x, "billete/s de 50")
else:
    print ("Ninguno de 50")

money_20 = money_50 % 20
money_20x = money_50 // 20

if money_20x > 0:
    print (money_20x, "billete/s de 20")
else:
    print ("Ninguno de 20")

money_10 = money_20 % 10
money_10x = money_20 // 10

if money_10x > 0:
    print (money_10x, "billete/s de 10")
else:
    print ("Ninguno de 10")

money_5 = money_10 % 5
money_5x = money_10 // 5

if money_5x > 0:
    print (money_5x, "billete/s de 5")
else:
    print ("Ninguno de 5")

money_2 = money_5 % 2
money_2x = money_5 // 2

if money_2x > 0:
    print (money_2x, "moneda/s de 2")
else:
    print ("Ninguno de 2")

money_1 = money_2 % 1
money_1x = money_2 // 1

if money_1x > 0:
    print (money_1x, "moneda/s de 1")
else:
    print ("Ninguno de 1")



