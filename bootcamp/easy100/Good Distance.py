import itertools

import math


def isSquare(n):
    ansN = math.floor(n ** 0.5)
    if n == ansN ** 2:
        return True
    else:
        return False


N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

p = itertools.combinations(X, 2)

kyori = 0
tmp_kyori = 0
cnt = 0
for v in p:
    # print(v)
    for i in range(len(v[0])):
        tmp_kyori += (v[0][i] - v[1][i])**2
        # print(v[0][i],  v[1][i])
    # print(tmp_kyori)
    kyori = tmp_kyori ** 0.5
    # print(kyori)
    if isSquare(tmp_kyori):
        cnt += 1
    tmp_kyori = 0

print(cnt)
