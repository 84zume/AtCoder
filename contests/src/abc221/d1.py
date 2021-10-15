N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]

t = [0] * ((10**9)*2)

maxDay = 0

for e in AB:
    t[e[0]] += 1
    t[e[0]+e[1]] -= 1
    maxDay = max(maxDay, e[0]+e[1])

for i in range(len(t)):
    if 0 < i:
        t[i] += t[i-1]

ans = [0] * N

print(t[:maxDay])
for i in range(maxDay):
    ans[t[i]] += 1

print(ans)
# 1000000000
