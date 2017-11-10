import sys
nota = float(sys.argv[1])
if nota >= 0 and nota <= 10:
  if nota < 5:
    print("Suspenso")
  if nota >= 5 and nota < 7:
    print("Aprobando")
  if nota >= 7 and nota < 9:
    print("Notable")
  if nota >= 9 and nota < 10:
    print("Sobresaliente")
  if nota == 10:
    print("Matrícula")
else:
    	print("Error introduzca una nota valida")
