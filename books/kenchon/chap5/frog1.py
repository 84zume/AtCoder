N = int(input())
h = list(map(int, input().split()))
print(h)

cost = [99999] * N
cost[0] = 0
# 最初の解き方
# for i in range(1, N):
#     if i == 1:
#         cost[i]=abs(h[1] - h[0])
#     elif i >= 2:
#         cost[i]=min(cost[i-1] + abs(h[i] - h[i-1]),
#                     cost[i-2] + abs(h[i] - h[i-2]))

# chminを利用する場合, 緩和（relaxation） →　これ聞きたいよ。
def chmin(dp, idx, b):
    if(dp[idx] > b):
        dp[idx] = b

# for i in range(1, N):
#     chmin(cost, i, cost[i-1] + abs(h[i] - h[i-1]))
#     if i > 1:
#         chmin(cost, i, cost[i-2] + abs(h[i] - h[i-2]))

# push-based
for i in range(N):
    if(i+1 < N):
        chmin(cost, i+1, cost[i] + abs(h[i+1] - h[i]))
    if(i+2 < N):
        chmin(cost, i+2, cost[i] + abs(h[i+2] - h[i]))

print(cost[-1])
print(cost)
