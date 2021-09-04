import math
X = int(input())

C = math.floor(X/100)
if X <= 105*C:
    print(1)
else:
    print(0)
