import bisect

N = int(input())
A = list(map(int, input().split()))
M = int(input())

A.append(0)

P = []

for i in range(len(A)):
    for j in range(len(A)):
        P.append(A[i] + A[j])
P.sort()

ans = 0
for p in P:
    index = bisect.bisect_left(P, M-p)
    if index == 0:
        continue
    ans = max(ans, p + P[index-1])
print(ans)
