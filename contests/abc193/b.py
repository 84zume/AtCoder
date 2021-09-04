N = int(input())
APX = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    APX[i][2] -= APX[i][0]

cost = 10000000000
for i in range(N):
    if APX[i][2] > 0:
        cost = min(cost, APX[i][1])

if cost == 10000000000:
    print(-1)
else:
    print(cost)
