import sys
import math

a = int(sys.argv[1])

b = int(sys.argv[2])

c = int(sys.argv[3])

if a == 0:
    x = -c / b
    print (x)
    
elif b**2 - 4*a*c < 0:
    
    print ("No tiene solución real")
    
else:
    
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    
    print ("x1 =", x1)
    print ("x2 =", x2)
