from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

A1 = []
for a in A:
    A1.append(a % 200)
# print(A1)
cnt = 0
for i in range(200):
    temp = A1.count(i)
    # print(i, temp)
    if temp > 1:
        cnt += cmb(temp, 2)
print(cnt)
