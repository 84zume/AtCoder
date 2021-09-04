import math

n, d = map(int, input().split())
p = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for e in p:
    dist = math.sqrt(e[0]**2 + e[1]**2)
    if dist <= d:
        cnt += 1
print(cnt)
