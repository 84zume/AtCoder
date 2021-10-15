N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]

cnt = 0
idx = 1

for i in range(N):
    for j in range(idx, N):
        # print(xy[i][1], xy[j][1], xy[i][0], xy[j][0])
        if (xy[i][0] - xy[j][0]) == 0:
            continue
        katamuki = (xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0])
        if -1 <= katamuki and katamuki <= 1:
            cnt += 1
    idx += 1

print(cnt)
