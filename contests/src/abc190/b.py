N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for i in range(N)]

for x in XY:
    if x[0] < S and x[1] > D:
        print('Yes')
        exit(0)

print('No')
