# 全部でN本、K本に電飾を付ける
N, K = map(int, input().split())
h = [int(input()) for i in range(N)]

sortedH = sorted(h, reverse=True)

minDiff = 1000000000
# print(sortedH)
for i in range(N-K+1):
    diff = sortedH[i] - sortedH[i+K-1]
    # print('i:', i, 'K:', K, 'diff: ', diff,
    #   'sortedH[i]: ', sortedH[i], 'sortedH[i+K-1]', sortedH[i+K-1])
    minDiff = min(minDiff, diff)
print(minDiff)
