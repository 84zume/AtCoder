N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]
# print(ab)
ans = [0]*N
for e in ab:
    ans[e[0]-1] += 1
    ans[e[1]-1] += 1

for e in ans:
    print(e)
