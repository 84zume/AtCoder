N = int(input())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

A = sorted(A)

used = [0]*N
count = 0

for i in range(N):
    maxy = -1
    maxid = -1
    for j in range(N):
        if used[j] == 1:
            continue

        if B[j][0] >= A[i][0]:
            continue

        if B[j][1] >= A[i][1]:
            continue

        maxy = max(B[j][1], maxy)

