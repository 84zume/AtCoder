N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for i in range(N+1)]

for i in range(N):
    for w in range(W):
        # iの荷物をいれる
        if w-wv[i][0] >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-wv[i][0]] + wv[i][1])
        # iの荷物を入れない
            dp[i+1][w] = max(dp[i+1][w], dp[i][w])
print(dp[-1][-1])