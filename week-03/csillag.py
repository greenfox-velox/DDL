for i in range(1, 7):
    print("*" * i)

for f in range(1, 7):
    g = 7
    print(" " * (g - f) + "*" * f)
    g -= 1

for g in range(7, 0, -1):
    print("*" * (g))

for h in range(7, 0, -1):
    g = 7
    print(" " * (g - h) + "*" * h)
    g -= 1

g = 10
f = 0
for j in range(1, 11):
    print(" " * g + "*" * (j + f))
    g -= 1
    f += 1

x = 0
y = 10

for k in range(11, 0, -1):
    print(" " * x + "*" * (k + y))
    x += 1
    y -= 1

for q in range(1, 2):
    g = 10
    f = 0
    for j in range(1, 11):
        print(" " * g + "*" * (j + f))
        g -= 1
        f += 1
    x = 0
    y = 10
    for k in range(11, 0, -1):
        print(" " * x + "*" * (k + y))
        x += 1
        y -= 1
