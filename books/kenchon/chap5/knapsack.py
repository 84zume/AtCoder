N = 6
W = 10
wegiht = [2, 1, 3, 6, 2, 1, 5]
value = [3, 2, 6, 1, 3, 85]

def chmax(l_a, idx1, idx2, b):
    if(l_a[idx1][idx2] < b):
        l_a[idx1][idx2] = b

dp = [[0] * (W+1) for i in range(N+1)]

print(dp)


for i in range(N):
    for w in range(W):
        if (w - wegiht[i] >= 0):
            chmax(dp, i+1, w, dp[i][w-wegiht[i]] + value[i])
        
        chmax(dp, i+1, w, dp[i][w])

print(dp[N][W])

print(dp)
