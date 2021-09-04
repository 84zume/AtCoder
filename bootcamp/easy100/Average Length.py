import itertools
N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]

p_xy = itertools.permutations(xy)

all = 0
cnt = 0

for l in p_xy:
    kyori = 0
    for i in range(1, len(l)):
        kyori += ((l[i][0]-l[i-1][0])**2 + (l[i][1]-l[i-1][1])**2)**0.5
    all += kyori
    cnt += 1

print(all/cnt)
