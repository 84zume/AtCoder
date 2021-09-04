import copy
N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for i in range(N)]
# 箱の価値
X = list(map(int, input().split()))
Qr = [list(map(int, input().split())) for i in range(Q)]

# OK
SortedWV = sorted(WV, key=lambda x: x[1], reverse=True)

# for s in SortedWV:
#     print(s)

for qr in Qr:
    UsableX = sorted(X[:qr[0]-1]+X[qr[1]:], reverse=False)
    # print(UsableX)
    sumval = 0
    tmp_WV = copy.deepcopy(SortedWV)
    tmp_X = copy.deepcopy(UsableX)
    for wv_i in range(len(tmp_WV)):
        for x_j in range(len(tmp_X)):
            if tmp_WV[wv_i][0] <= tmp_X[x_j]:
                # print('IN ', SortedWV[wv_i], UsableX[x_j])
                sumval += tmp_WV[wv_i][1]
                tmp_WV[wv_i][0] = 10000000
                tmp_X[x_j] = -1
    print(sumval)
