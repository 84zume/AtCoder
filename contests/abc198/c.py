import math
R, X, Y = map(int, input().split())

kyori = (X**2 + Y**2)**0.5

# print(kyori)
# print(R)
if kyori/R < 1.0:
    print(2)
else:
    hosuu = math.ceil(kyori / R)
    print(hosuu)
