import sys

n = int(input())
d = [list(map(int, input().split())) for i in range(n)]

cnt = 0

for e in d:
    if (e[0] + e[1])/2 == e[0]:
        cnt = cnt + 1
        if cnt == 3:
            print("Yes")
            sys.exit()
    else:
        cnt = 0

print("No")
