import math
a, b, c = map(int, input().split())

n = math.ceil(a/c)

if c * n <= b:
    print(c * n)
else:
    print(-1)
