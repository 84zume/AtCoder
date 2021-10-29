N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    # push-based
    for k in range(1, K+1):
        if i + k < N:
            dp[i+k] = min(dp[i+k], dp[i] + abs(h[i+k] - h[i]))
        else:
            break

print(dp[-1])