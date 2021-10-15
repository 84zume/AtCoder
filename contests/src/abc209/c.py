N = int(input())
C = list(map(int, input().split()))
C = sorted(C)
s = C[0]
for i in range(1, N):
    s *= (C[i]-i)
    # print(C[i]-i)
    # print(s)
    if s > 10**9+7:
        s = s % (10**9+7)

print(s % (10**9+7))
