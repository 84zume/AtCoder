from bisect import bisect_left, bisect_right


def getNearestIndex(list, num):
    idx = bisect_left(list, num)
    return idx


def cut(W, position):
    i = getNearestIndex(W, position)
    W.insert(i, position)


def show(W, position):
    i = getNearestIndex(W, position)
    print(W[i] - W[i-1])


L, Q = map(int, input().split())
C = []
for i in range(Q):
    c, x = map(int, input().split())
    C.append([c, x])

Wood = [0, L]

for c in C:
    if c[0] == 1:
        cut(Wood, c[1])
    else:
        show(Wood, c[1])
