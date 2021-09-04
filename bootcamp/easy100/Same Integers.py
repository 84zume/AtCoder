import math
X = list(map(int, input().split()))
X.sort()

a = X[2] - X[0]
b = X[2] - X[1]

if(a-b) % 2 == 0:
    print(int((a+b)/2))
else:
    print(int(1+((a+b+1)/2)))
