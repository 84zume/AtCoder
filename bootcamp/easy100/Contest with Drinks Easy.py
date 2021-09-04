N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for x in range(M)]


for p in PX:
    ans = 0
    for i in range(N):
        plus = T[i]
        if p[0] == i+1:
            plus = p[1]
        ans += plus
    print(ans)


# for t in T:
#     plus = t
#     for p in PX:
