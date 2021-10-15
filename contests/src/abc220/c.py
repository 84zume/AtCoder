import math
from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))
X = int(input())

allA = sum(A)
# print('allA', allA)
preindexX = math.floor(Fraction(str(X))/Fraction(str(allA)))
# print('preindexX', preindexX)


idx = N * preindexX
now = allA * preindexX

# print(idx, now)

for i in range(len(A)):
    idx += 1
    now += A[i]
    if now > X:
        break
print(idx)
