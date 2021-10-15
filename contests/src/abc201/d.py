H, W = map(int, input().split())
A = [list(input()) for i in range(W)]


def dfs():
    return list(_dfs(0, 0))


def _dfs(i, j):
    print(i, j)
    if i == H-1 and j == W-1:
        print('hoge', i, j, A[2][2])
        yield [A[i][j]]
    else:
        if (i < H-1):
            for path in _dfs(i+1, j):
                yield [A[i][j]] + path
        if (j < W-1):
            for path in _dfs(i, j+1):
                yield [A[i][j]] + path
