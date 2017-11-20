import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
a = 0
t = 0
g = 0
c = 0
for i in (sequence):
    if i == "A":
        a += 1
    elif i == "T":
        t += 1
    elif i == "G":
        g += 1
    elif i == "C":
        c += 1
print(f"Adedine:{a}\nThymine:{t}\nGuanine:{g}\nCytosine:{c}")
