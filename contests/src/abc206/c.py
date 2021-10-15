def func(n):
    return int((n*(n-1))/2)


N = int(input())
A = list(map(int, input().split()))

countA = {}
for a in A:
    if a in countA:
        countA[a] += 1
    else:
        countA[a] = 1

sa = 0

for a in countA.values():
    if a >= 2:
        sa += func(a)

maxC = func(N)

print(maxC-sa)
