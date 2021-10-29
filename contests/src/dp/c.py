N = int(input())
a = [list(map(int, input().split())) for i in range(N)]

dp = [[0, 0, 0] for _ in range(N)]

for i in range(3):
    dp[0][i] = a[0][i]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + a[i][j]) 
print(max(dp[-1]))